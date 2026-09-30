using UnityEngine;

public class DoorWallBuilder : MonoBehaviour
{
    [Header("Doorway Size")]
    public float wallWidth = 15f;
    public float wallHeight = 5f;
    public float wallThickness = 0.2f;

    public float doorWidth = 2.5f;
    public float doorHeight = 3f;

    [Header("Wall Position")]
    public float wallZ = 7.5f;

    private void Start()
    {
        // If a polished architectural wall is already configured, do not spawn duplicate untextured blocks
        var polishedRoot = GameObject.Find("_VISUAL_POLISH_V16_") ?? GameObject.Find("_VISUAL_POLISH_V15_");
        if (polishedRoot != null)
            return;

        BuildDoorWall();
    }

    private void BuildDoorWall()
    {
        float sideWidth = (wallWidth - doorWidth) / 2f;
        float topHeight = wallHeight - doorHeight;

        Material wallMat = null;
        var rend = GetComponentInChildren<Renderer>();
        if (rend != null) wallMat = rend.sharedMaterial;

        // LEFT WALL
        GameObject leftWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        leftWall.name = "BackWallLeft";
        leftWall.transform.position = new Vector3(-(doorWidth / 2f + sideWidth / 2f), wallHeight / 2f, wallZ);
        leftWall.transform.localScale = new Vector3(sideWidth, wallHeight, wallThickness);
        if (wallMat) leftWall.GetComponent<Renderer>().sharedMaterial = wallMat;

        // RIGHT WALL
        GameObject rightWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        rightWall.name = "BackWallRight";
        rightWall.transform.position = new Vector3((doorWidth / 2f + sideWidth / 2f), wallHeight / 2f, wallZ);
        rightWall.transform.localScale = new Vector3(sideWidth, wallHeight, wallThickness);
        if (wallMat) rightWall.GetComponent<Renderer>().sharedMaterial = wallMat;

        // TOP WALL
        GameObject topWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        topWall.name = "BackWallTop";
        topWall.transform.position = new Vector3(0f, doorHeight + topHeight / 2f, wallZ);
        topWall.transform.localScale = new Vector3(doorWidth, topHeight, wallThickness);
        if (wallMat) topWall.GetComponent<Renderer>().sharedMaterial = wallMat;
    }
}