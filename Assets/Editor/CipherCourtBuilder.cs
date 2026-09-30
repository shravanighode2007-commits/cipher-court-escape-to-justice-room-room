#if UNITY_EDITOR
using System;
using System.IO;
using System.Linq;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEngine;

public static class CipherCourtBuilder
{
    private static readonly string[] RequiredScenes = new[]
    {
        "Assets/Scenes/MainMenu.unity",
        "Assets/Scenes/Level1_Investigation.unity",
        "Assets/Scenes/Level2_Computer.unity",
        "Assets/Scenes/Level3_Evidence.unity",
        "Assets/Scenes/Level4_Archive.unity",
        "Assets/Scenes/Level5_CaseFiles.unity",
        "Assets/Scenes/Level6_FinalVerdict.unity",
        "Assets/Scenes/GameComplete.unity"
    };

    private const string OutputFolder = "Builds/CipherCourt_Windows_x64";
    private const string ExecutableName = "CipherCourt.exe";

    [MenuItem("Cipher Court/Build Standalone Player (Windows x64)")]
    public static void BuildMenu()
    {
        PerformBuild(isBatchMode: false);
    }

    public static void BuildWindowsStandalone()
    {
        PerformBuild(isBatchMode: true);
    }

    private static void PerformBuild(bool isBatchMode)
    {
        Debug.Log("==================================================");
        Debug.Log("  CIPHER COURT - WINDOWS X64 STANDALONE BUILDER   ");
        Debug.Log("==================================================");

        // 1. Verify all required scenes exist
        foreach (string scenePath in RequiredScenes)
        {
            if (!File.Exists(scenePath))
            {
                string error = $"[Build Error] Missing required scene: {scenePath}";
                Debug.LogError(error);
                if (isBatchMode) EditorApplication.Exit(1);
                return;
            }
            Debug.Log($"[Build OK] Scene verified: {scenePath}");
        }

        // 2. Configure Player Settings
        PlayerSettings.companyName = "Sahil Kate";
        PlayerSettings.productName = "Cipher Court - Escape to Justice";
        PlayerSettings.defaultScreenWidth = 1920;
        PlayerSettings.defaultScreenHeight = 1080;
        PlayerSettings.fullScreenMode = FullScreenMode.FullScreenWindow;
        PlayerSettings.resizableWindow = true;
        PlayerSettings.runInBackground = true;

        // 3. Prepare output directory
        string fullOutputDir = Path.GetFullPath(OutputFolder);
        if (!Directory.Exists(fullOutputDir))
        {
            Directory.CreateDirectory(fullOutputDir);
        }

        string fullOutputPath = Path.Combine(fullOutputDir, ExecutableName);

        // 4. Configure Build Options
        BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions
        {
            scenes = RequiredScenes,
            locationPathName = fullOutputPath,
            target = BuildTarget.StandaloneWindows64,
            options = BuildOptions.None
        };

        Debug.Log($"Starting Standalone Windows 64-bit build to: {fullOutputPath}");
        DateTime startTime = DateTime.Now;

        BuildReport report = BuildPipeline.BuildPlayer(buildPlayerOptions);
        BuildSummary summary = report.summary;

        TimeSpan duration = DateTime.Now - startTime;

        if (summary.result == BuildResult.Succeeded)
        {
            Debug.Log("==================================================");
            Debug.Log($"BUILD SUCCEEDED in {duration.TotalSeconds:F2} seconds!");
            Debug.Log($"Total Size: {summary.totalSize / (1024 * 1024)} MB");
            Debug.Log($"Output Path: {fullOutputPath}");
            Debug.Log("==================================================");

            if (isBatchMode) EditorApplication.Exit(0);
        }
        else
        {
            Debug.LogError("==================================================");
            Debug.LogError($"BUILD FAILED with result: {summary.result}");
            Debug.LogError($"Errors: {summary.totalErrors}, Warnings: {summary.totalWarnings}");
            Debug.LogError("==================================================");

            if (isBatchMode) EditorApplication.Exit(1);
        }
    }

    [MenuItem("Cipher Court/Build WebGL (Live Browser Online Play)")]
    public static void BuildWebGLMenu()
    {
        PerformWebGLBuild(isBatchMode: false);
    }

    public static void BuildWebGL()
    {
        PerformWebGLBuild(isBatchMode: true);
    }

    private static void PerformWebGLBuild(bool isBatchMode)
    {
        Debug.Log("==================================================");
        Debug.Log("  CIPHER COURT - WEBGL LIVE ONLINE PLAYER BUILDER ");
        Debug.Log("==================================================");

        string outputFolder = "Builds/CipherCourt_WebGL";
        string fullOutputDir = Path.GetFullPath(outputFolder);
        if (!Directory.Exists(fullOutputDir))
        {
            Directory.CreateDirectory(fullOutputDir);
        }

        PlayerSettings.WebGL.compressionFormat = WebGLCompressionFormat.Disabled;
        PlayerSettings.WebGL.decompressionFallback = false;

        BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions
        {
            scenes = RequiredScenes,
            locationPathName = fullOutputDir,
            target = BuildTarget.WebGL,
            options = BuildOptions.None
        };

        Debug.Log($"Starting WebGL build to: {fullOutputDir}");
        DateTime startTime = DateTime.Now;

        BuildReport report = BuildPipeline.BuildPlayer(buildPlayerOptions);
        BuildSummary summary = report.summary;
        TimeSpan duration = DateTime.Now - startTime;

        if (summary.result == BuildResult.Succeeded)
        {
            Debug.Log("==================================================");
            Debug.Log($"WEBGL BUILD SUCCEEDED in {duration.TotalSeconds:F2} seconds!");
            Debug.Log($"Total Size: {summary.totalSize / (1024 * 1024)} MB");
            Debug.Log($"Output Path: {fullOutputDir}");
            Debug.Log("==================================================");

            if (isBatchMode) EditorApplication.Exit(0);
        }
        else
        {
            Debug.LogError("==================================================");
            Debug.LogError($"WEBGL BUILD FAILED with result: {summary.result}");
            Debug.LogError($"Errors: {summary.totalErrors}, Warnings: {summary.totalWarnings}");
            Debug.LogError("==================================================");

            if (isBatchMode) EditorApplication.Exit(1);
        }
    }
}
#endif
