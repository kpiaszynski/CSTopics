#echo.py

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    text = text[-repetitions:]
    response = []

    for i in range(repetitions):
        response.append(text[i:])
    response.append(".")
    
    return("\n".join(response))


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

