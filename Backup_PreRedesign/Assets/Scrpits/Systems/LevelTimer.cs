using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;

public class LevelTimer : MonoBehaviour
{
    [SerializeField] private float timeRemaining = 300f;
    [SerializeField] private TMP_Text timerText;
    [SerializeField] private GameObject levelFailedPanel;

    [Header("Time Penalty")]
    [SerializeField] private float overtimeExtension = 60f;
    [SerializeField] private int scorePenalty = 100;

    private bool timerRunning = true;
    private int timePenalties = 0;

    private void Start()
    {
        if (levelFailedPanel != null)
            levelFailedPanel.SetActive(false);

        UpdateTimerDisplay();
    }

    private void Update()
    {
        if (!timerRunning)
            return;

        timeRemaining -= Time.deltaTime;

        if (timeRemaining <= 0f)
        {
            ApplyTimePenalty();
        }

        UpdateTimerDisplay();
    }

    private void ApplyTimePenalty()
    {
        timePenalties++;
        timeRemaining = Mathf.Max(30f, overtimeExtension);

        if (GameManager.Instance != null)
            GameManager.Instance.DeductScore(scorePenalty);

        PopupFeedback.Show("TIME EXPIRED - PENALTY APPLIED\n+60 SECONDS", false, 2.4f);
        CipherCourtDatabase.LogEvent("time_penalty", "penalty", "Timer expired; extra time granted");
    }

    private void UpdateTimerDisplay()
    {
        if (timerText == null) return;

        int minutes = Mathf.FloorToInt(timeRemaining / 60f);
        int seconds = Mathf.FloorToInt(timeRemaining % 60f);
        timerText.text = $"{minutes:00}:{seconds:00}";
    }

    public void StopTimer()
    {
        timerRunning = false;
    }

    // Kept for attempt-based failure systems. Timer expiration no longer calls this.
    public void FailLevel()
    {
        timerRunning = false;

        if (levelFailedPanel != null)
            levelFailedPanel.SetActive(true);

        Time.timeScale = 0f;
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
        CipherCourtDatabase.LogEvent("level_failed", "failed", "Attempts exhausted");
    }

    public void RetryLevel()
    {
        Time.timeScale = 1f;
        Scene currentScene = SceneManager.GetActiveScene();
        SceneManager.LoadScene(currentScene.name);
    }

    public void MainMenu()
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene("MainMenu");
    }
}
