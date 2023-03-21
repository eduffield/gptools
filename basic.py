import openai

openai.api_key = "PASTE_OPENAI_TOKEN"

def listmodels():
    models = openai.Model.list()
    model_names = [model.id for model in models["data"]]
    for model in model_names:
        print(model)

def query(userprompt):
    response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=userprompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5)
    return response.choices[0].text.strip()
    
def imgquery(userprompt):
    response = openai.Image.create(prompt=userprompt,
                                    n=1,
                                    size="512x512")
    image_url = response['data'][0]['url']
    return image_url
	
if __name__ == "__main__":
    listmodels()
    print()
    print(query("Write a book report on a Tolstoy novel."))
    print()
    print(imgquery("Avocado chair"))
    print()
