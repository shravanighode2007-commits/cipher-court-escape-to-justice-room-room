using UnityEngine;
using UnityEngine.InputSystem;
using TMPro;

public class Level5File : MonoBehaviour
{
    [Header("File Settings")]
    public int fileNumber = 1;
    public string fileValue = "3";

    [Header("UI")]
    public TMP_Text interactionText;

    private Vector3 initialPos;
    private bool playerNearby = false;
    private bool collected = false;

    void Start()
    {
        initialPos = transform.position;

        SphereCollider col = GetComponent<SphereCollider>();
        if (col == null) col = gameObject.AddComponent<SphereCollider>();
        col.isTrigger = true;
        col.radius = 2.2f;

        Rigidbody rb = GetComponent<Rigidbody>();
        if (rb == null) rb = gameObject.AddComponent<Rigidbody>();
        rb.isKinematic = true;
        rb.useGravity = false;

        if (interactionText != null)
            interactionText.gameObject.SetActive(false);
    }

    void Update()
    {
        if (collected) return;

        // Visual bobbing and spinning
        float newY = initialPos.y + Mathf.Sin(Time.time * 2.5f) * 0.08f;
        transform.position = new Vector3(initialPos.x, newY, initialPos.z);
        transform.Rotate(Vector3.up, 35f * Time.deltaTime, Space.World);

        bool ePressed = false;
        try { if (Input.GetKeyDown(KeyCode.E)) ePressed = true; } catch {}
        try { if (Keyboard.current != null && Keyboard.current.eKey.wasPressedThisFrame) ePressed = true; } catch {}

        if (playerNearby && ePressed)
        {
            CollectFile();
        }
    }

    void CollectFile()
    {
        if (collected) return;
        collected = true;

        Level5CasePuzzle puzzle = FindFirstObjectByType<Level5CasePuzzle>();

        if (puzzle != null)
        {
            puzzle.CollectFile(fileNumber, fileValue);
        }

        PopupFeedback.Show($"CASE STATEMENT #{fileNumber} INSPECTED!", true);
        CipherCourtDatabase.LogEvent("clue_collected", "success", $"Case Statement #{fileNumber}");

        if (interactionText != null)
            interactionText.gameObject.SetActive(false);

        CleanUpBeacon();
        gameObject.SetActive(false);
    }

    private void CleanUpBeacon()
    {
        GameObject root = GameObject.Find("_VISUAL_POLISH_V13_");
        if (root != null)
        {
            foreach (Transform child in root.transform)
            {
                if (child.name.StartsWith("ClueBeacon_") && Vector3.Distance(child.position, transform.position) < 2.5f)
                {
                    Destroy(child.gameObject);
                }
            }
        }
    }

    void OnTriggerEnter(Collider other)
    {
        if (IsPlayer(other))
        {
            playerNearby = true;

            if (interactionText != null)
            {
                interactionText.text = "Press E to inspect file";
                interactionText.gameObject.SetActive(true);
            }

            CollectFile();
        }
    }

    void OnTriggerStay(Collider other)
    {
        if (!collected && IsPlayer(other))
        {
            playerNearby = true;
        }
    }

    void OnTriggerExit(Collider other)
    {
        if (IsPlayer(other))
        {
            playerNearby = false;

            if (interactionText != null)
                interactionText.gameObject.SetActive(false);
        }
    }

    bool IsPlayer(Collider other)
    {
        if (other == null) return false;
        if (other.CompareTag("Player") || other.transform.root.CompareTag("Player")) return true;
        if (other.GetComponentInParent<CharacterController>() != null) return true;
        if (other.name.ToLower().Contains("player")) return true;
        return false;
    }
}