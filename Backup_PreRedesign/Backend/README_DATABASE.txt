CIPHER COURT - POSTGRESQL DATABASE

1. Create a PostgreSQL database named: cipher_court
2. Set your password in DATABASE_URL, or run CMD:
   set DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/cipher_court
3. In this Backend folder run:
   pip install -r requirements.txt
   python -m uvicorn main:app --reload
4. Test in browser:
   http://127.0.0.1:8000/health
5. Keep the backend running while playing the Unity game.

The game continues normally even when the database API is offline. Events are simply skipped with a warning in the Unity Console.
