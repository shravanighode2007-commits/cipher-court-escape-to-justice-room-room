using System.Collections;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class PopupFeedback : MonoBehaviour
{
    private static PopupFeedback instance;
    private Canvas canvas;
    private Image panel;
    private TMP_Text text;
    private Coroutine routine;

    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]
    private static void Bootstrap()
    {
        if (instance != null) return;
        GameObject go = new GameObject("PopupFeedbackSystem");
        instance = go.AddComponent<PopupFeedback>();
        DontDestroyOnLoad(go);
        instance.BuildUI();
    }

    private void BuildUI()
    {
        canvas = gameObject.AddComponent<Canvas>();
        canvas.renderMode = RenderMode.ScreenSpaceOverlay;
        canvas.sortingOrder = 5000;
        gameObject.AddComponent<CanvasScaler>();
        gameObject.AddComponent<GraphicRaycaster>();

        GameObject panelGO = new GameObject("PopupPanel");
        panelGO.transform.SetParent(transform, false);
        panel = panelGO.AddComponent<Image>();
        panel.color = new Color(0.025f, 0.05f, 0.08f, 0.96f);
        RectTransform pr = panel.rectTransform;
        pr.anchorMin = new Vector2(0.5f, 0.72f);
        pr.anchorMax = new Vector2(0.5f, 0.72f);
        pr.pivot = new Vector2(0.5f, 0.5f);
        pr.sizeDelta = new Vector2(620f, 110f);

        GameObject textGO = new GameObject("PopupText");
        textGO.transform.SetParent(panelGO.transform, false);
        text = textGO.AddComponent<TextMeshProUGUI>();
        text.fontSize = 30f;
        text.fontStyle = FontStyles.Bold;
        text.alignment = TextAlignmentOptions.Center;
        text.color = Color.white;
        RectTransform tr = text.rectTransform;
        tr.anchorMin = Vector2.zero;
        tr.anchorMax = Vector2.one;
        tr.offsetMin = new Vector2(24f, 12f);
        tr.offsetMax = new Vector2(-24f, -12f);

        panelGO.SetActive(false);
    }

    public static void Show(string message, bool success, float seconds = 1.8f)
    {
        if (instance == null)
        {
            Bootstrap();
        }
        if (instance == null) return;
        instance.Display(message, success, seconds);
    }

    private void Display(string message, bool success, float seconds)
    {
        if (panel == null || text == null) BuildUI();
        text.text = message;
        text.color = success ? new Color(0.35f, 1f, 0.62f) : new Color(1f, 0.42f, 0.36f);
        panel.gameObject.SetActive(true);
        if (routine != null) StopCoroutine(routine);
        routine = StartCoroutine(HideAfter(seconds));
    }

    private IEnumerator HideAfter(float seconds)
    {
        yield return new WaitForSecondsRealtime(seconds);
        if (panel != null) panel.gameObject.SetActive(false);
        routine = null;
    }
}
