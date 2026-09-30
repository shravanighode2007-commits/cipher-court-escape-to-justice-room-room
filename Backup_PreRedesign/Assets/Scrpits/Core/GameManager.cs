using UnityEngine;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    [Header("Game State")]
    [SerializeField] private int currentLevel = 1;
    [SerializeField] private int score = 0;
    [SerializeField] private bool gameRunning = false;

    public int CurrentLevel => currentLevel;
    public int Score => score;
    public bool GameRunning => gameRunning;

    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }

        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

    private void Start()
    {
        StartGame();
    }

    public void StartGame()
    {
        currentLevel = 1;
        score = 0;
        gameRunning = true;

        Debug.Log("Cipher Court started.");
    }

    public void AddScore(int points)
    {
        if (points <= 0) return;

        score += points;
        Debug.Log("Score: " + score);
    }

    public void DeductScore(int points)
    {
        if (points <= 0) return;

        score = Mathf.Max(0, score - points);
        Debug.Log("Score: " + score);
    }

    public void CompleteLevel()
    {
        currentLevel++;
        Debug.Log("Level completed. Next level: " + currentLevel);
    }

    public void GameOver()
    {
        gameRunning = false;
        Debug.Log("Game Over.");
    }

    public void Victory()
    {
        gameRunning = false;
        Debug.Log("Cipher Court completed!");
    }
}