from flask import Flask, render_template, request

app = Flask(__name__)

def obter_links(option):
    links = {
        'YOUTUBE': 'https://www.youtube.com/',
        'INSTAGRAM': 'https://www.instagram.com/',
        'FACEBOOK': 'https://www.facebook.com/',
        'TWITTER': 'https://www.twitter.com/',
        'GITHUB': 'https://www.github.com/',
        'MOJANG': 'https://www.mojang.com/'
    }
    return links.get(option, 'Opção inválida')

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    if request.method == 'POST':

        # Pega o valor que veio do HTML (pelo 'name' do input)
        opcao_usuario = request.form.get('nome_do_input').upper()
        resultado = obter_links(opcao_usuario)
    
    # O Python "renderiza" o HTML e envia a variável 'resultado' para ele
    return render_template('index.html', link_final=resultado)

if __name__ == '__main__':
    app.run(debug=True)