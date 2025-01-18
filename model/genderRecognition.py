from deepface import DeepFace

def face_analyzer(frame):
    """Analiza un cuadro para género, edad y emoción."""
    try:
        # Select the characteristics to analyze with deepface
        analysis = DeepFace.analyze(frame, actions=["gender", "age", "emotion"], enforce_detection=False)

        if not analysis:
            print("No face detected!")
            return None, None, None

        # Only show the first face detected
        if isinstance(analysis, list) and len(analysis) > 0:
            analysis = analysis[0]  # Obtén el primer rostro

        # select the data
        gender = analysis["dominant_gender"]
        age = int(analysis["age"])
        emotion = analysis["dominant_emotion"]

        print(f"Analysis result: {analysis}")


        return gender, age, emotion

    except Exception as e:
        print(f"Face analysis error: {e}")
        return None, None, None
