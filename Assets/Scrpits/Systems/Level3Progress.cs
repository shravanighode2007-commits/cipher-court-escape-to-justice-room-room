using UnityEngine;
using TMPro;

public class Level3Progress : MonoBehaviour
{
    [SerializeField] private TMP_Text evidenceCollectedText;

    public bool HasEvidenceA { get; private set; }
    public bool HasEvidenceB { get; private set; }
    public bool HasEvidenceC { get; private set; }

    public void CollectEvidenceA()
    {
        HasEvidenceA = true;
        ShowMessage("4 COLLECTED");
    }

    public void CollectEvidenceB()
    {
        HasEvidenceB = true;
        ShowMessage("7 COLLECTED");
    }

    public void CollectEvidenceC()
    {
        HasEvidenceC = true;
        ShowMessage("2 COLLECTED");
    }

    public bool HasAllEvidence()
    {
        return HasEvidenceA && HasEvidenceB && HasEvidenceC;
    }

    private void ShowMessage(string message)
    {
        if (evidenceCollectedText == null)
            return;

        evidenceCollectedText.text = message;
        evidenceCollectedText.gameObject.SetActive(true);

        CancelInvoke(nameof(HideMessage));
        Invoke(nameof(HideMessage), 2f);
    }

    private void HideMessage()
    {
        if (evidenceCollectedText != null)
            evidenceCollectedText.gameObject.SetActive(false);
    }
}