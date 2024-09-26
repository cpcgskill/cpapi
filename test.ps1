$MAYA_BIN_ROOT = "C:\Program Files\Autodesk"

if ($args[0] -eq "run") {
    $env:PYTHONPATH = "./scripts/test;./src;${env:PYTHONPATH}"
    foreach ($maya_version in 2018, 2019, 2020, 2022, 2023, 2024, 2025) {
        $mayapy = "${MAYA_BIN_ROOT}\Maya$maya_version\bin\mayapy.exe"
        & $mayapy ./scripts/test/test_all.py
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Maya $maya_version test failed"
            exit 1
        }
        Write-Host "Maya $maya_version test passed"
    }
}
elseif ($args[0] -eq "install") {
    foreach ($maya_version in 2018, 2019, 2020, 2022, 2023, 2024, 2025) {
        $mayapy = "${MAYA_BIN_ROOT}\Maya$maya_version\bin\mayapy.exe"
        & $mayapy -m pip install -t ./temp cpapi -f dist
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to install cpapi for Maya $maya_version"
            exit 1
        }
        Remove-Item -Recurse -Force "./temp"
    }
}
else{
    Write-Error "Invalid argument"
    exit 1
}