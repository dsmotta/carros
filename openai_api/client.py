from google import genai
from google.genai import types


def car_gemini_ai(model, brand, year):

    client = genai.Client(api_key='AIzaSyClLB1mKRtSE4q-4SQbCBr0N_0J00GFHKg')

    message='''' Elaborar um resumo sobre o veiculo {} marca {} ano {} com 200 caracteres. '''

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[message.format(model, brand, year)],
        config=types.GenerateContentConfig(max_output_tokens=1000)
    )
    return response.text
    
    