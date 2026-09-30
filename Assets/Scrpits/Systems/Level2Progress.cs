using UnityEngine;

public class Level2Progress : MonoBehaviour
{
    public bool HasPasswordClue { get; private set; }

    public void CollectPasswordClue()
    {
        HasPasswordClue = true;

        Debug.Log("PASSWORD CLUE COLLECTED");
        Debug.Log("CLUE: COURT + 2026");
    }

    public bool CanUseComputer()
    {
        return HasPasswordClue;
    }
}