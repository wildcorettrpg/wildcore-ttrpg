# Velocity TTRPG — File Integrity Check
# Run from the repo root in PowerShell:
#   .\verify_integrity.ps1
#
# Checks every .md file under Core Rules/ for signs of corruption:
#   1. Null bytes          — always wrong; indicates Edit tool corruption
#   2. No trailing newline — every well-formed .md file ends with one
#   3. Broken last line    — file ends mid-link, mid-table-row, or mid-emphasis

$coreRules = Join-Path $PSScriptRoot "Core Rules"
$total = 0
$problems = @()

Get-ChildItem -Path $coreRules -Recurse -Filter "*.md" | Sort-Object FullName | ForEach-Object {
    $total++
    $file = $_.FullName
    $rel  = $file.Substring($PSScriptRoot.Length + 1)
    $fileIssues = @()

    $bytes = [System.IO.File]::ReadAllBytes($file)

    # 1. Null bytes
    $nullCount = ($bytes | Where-Object { $_ -eq 0 }).Count
    if ($nullCount -gt 0) {
        $fileIssues += "NULL BYTES: $nullCount null bytes found"
    }

    # 2. Trailing newline (last byte should be 0x0A)
    if ($bytes.Length -gt 0 -and $bytes[-1] -ne 0x0A) {
        $tail = [System.Text.Encoding]::UTF8.GetString($bytes[[Math]::Max(0, $bytes.Length - 60)..($bytes.Length - 1)])
        $fileIssues += "NO TRAILING NEWLINE — last 60 chars: $tail"
    }

    # 3. Broken last line — check the last non-empty line for open constructs
    $text = [System.Text.Encoding]::UTF8.GetString($bytes)
    $lastLine = ($text -split "`n" | Where-Object { $_.Trim() -ne "" } | Select-Object -Last 1)
    if ($lastLine) {
        $trimmed = $lastLine.TrimEnd()
        # Open markdown link: ends with ]( without a closing )
        if ($trimmed -match '\]\([^\)]*$') {
            $fileIssues += "OPEN LINK on last line: $trimmed"
        }
        # Open emphasis: odd number of ** (unclosed bold)
        elseif (([regex]::Matches($trimmed, '\*\*')).Count % 2 -ne 0) {
            $fileIssues += "UNCLOSED BOLD on last line: $trimmed"
        }
        # Open table row: starts with | but doesn't end with |
        elseif ($trimmed.StartsWith('|') -and -not $trimmed.EndsWith('|')) {
            $fileIssues += "INCOMPLETE TABLE ROW on last line: $trimmed"
        }
    }

    if ($fileIssues.Count -gt 0) {
        $problems += [PSCustomObject]@{ File = $rel; Issues = $fileIssues }
    }
}

Write-Host "Velocity TTRPG File Integrity Check"
Write-Host "Scanned $total .md files in Core Rules/"
Write-Host ""

if ($problems.Count -eq 0) {
    Write-Host "All files clean." -ForegroundColor Green
    exit 0
} else {
    Write-Host "PROBLEMS IN $($problems.Count) FILE(S):" -ForegroundColor Red
    Write-Host ""
    foreach ($p in $problems) {
        Write-Host "  $($p.File)" -ForegroundColor Yellow
        foreach ($issue in $p.Issues) {
            Write-Host "    - $issue"
        }
    }
    exit 1
}
