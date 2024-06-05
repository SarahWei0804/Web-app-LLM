
## Download Ollama
First, download Ollama according to your operation system. If you're using Windows or MacOS system, get Ollama from the [official website](https://ollama.com/download). If you're using Linux system, get Ollama with following command line:

```bash=
curl -fsSL https://ollama.com/install.sh | sh
```
Next, start Ollama to download LLM models.

## Get the LLM models
There are sevral popular LLM models listed on Ollama, ex. Llama 2, mistral, Gemma, etc. You can view all the models [here](https://ollama.com/library). In this example, I will use Llama 3. Let's get the model.

<img width="842" alt="image" src="https://github.com/SarahWei0804/Web-app-LLM/assets/69449635/a3c31d64-681d-43a8-999b-eb0f6cd6d7b8">

Llama 3 has different versions for use. We'll get the latest version for demo.
```bash=
ollama pull llama3:latest
```
After finish pulling the model, we can see the downloaded models by following command
```bash=
ollama list
```

Now, we can apply Llama 3 with Streamlit locally.

## Python: app.py
Before run app.py, install the required packges.
```bash=
pip install -r requirements.txt
```
Next, run app.py with streamlit command.

```bash=
streamlit run app.py
```

<img width="808" alt="image" src="https://github.com/SarahWei0804/Web-app-LLM/assets/69449635/3277db51-80b3-4bb6-a424-33087600ed5e">

You'll see the interactive textbox with Llama3.


