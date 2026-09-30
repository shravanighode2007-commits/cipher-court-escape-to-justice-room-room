using UnityEngine;
using UnityEngine.InputSystem;

public class PasswordPuzzleInteraction : MonoBehaviour
{
    [SerializeField] private PasswordPuzzleUI puzzleUI;
    [SerializeField] private Transform player;
    [SerializeField] private GameObject interactionText;
    [SerializeField] private GameObject requirementText;
    [SerializeField] private float interactionDistance = 3f;

    private Level2Progress progress;
    private bool puzzleOpen = false;

    private void Start()
    {
        if (player != null)
            progress = player.GetComponent<Level2Progress>();

        if (interactionText != null)
            interactionText.SetActive(false);

        if (requirementText != null)
            requirementText.SetActive(false);
    }

    private void Update()
    {
        if (player == null || puzzleUI == null || progress == null)
            return;

        float distance = Vector3.Distance(
            player.position,
            transform.position
        );

        bool playerIsNear = distance <= interactionDistance;

        if (interactionText != null)
        {
            interactionText.SetActive(
                playerIsNear && !puzzleOpen
            );
        }

        if (playerIsNear &&
            !puzzleOpen &&
            Keyboard.current != null &&
            Keyboard.current.eKey.wasPressedThisFrame)
        {
            if (!progress.CanUseComputer())
            {
                if (requirementText != null)
                {
                    requirementText.SetActive(true);

                    CancelInvoke(nameof(HideRequirementText));
                    Invoke(nameof(HideRequirementText), 2f);
                }

                return;
            }

            puzzleOpen = true;

            if (interactionText != null)
                interactionText.SetActive(false);

            if (requirementText != null)
                requirementText.SetActive(false);

            puzzleUI.OpenPuzzle();
        }
    }

    private void HideRequirementText()
    {
        if (requirementText != null)
            requirementText.SetActive(false);
    }

    public void PuzzleClosed()
    {
        puzzleOpen = false;
    }
}