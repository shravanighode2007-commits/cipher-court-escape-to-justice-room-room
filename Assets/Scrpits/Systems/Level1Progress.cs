using UnityEngine;

public class Level1Progress : MonoBehaviour
{
    public bool HasClue { get; private set; }
    public bool HasKey { get; private set; }

    public void CollectClue()
    {
        HasClue = true;
        Debug.Log("Clue collected.");
    }

    public void CollectKey()
    {
        HasKey = true;
        Debug.Log("Key collected.");
    }

    public bool CanUsePuzzle()
    {
        return HasClue && HasKey;
    }
}