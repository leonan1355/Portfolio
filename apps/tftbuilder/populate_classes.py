from apps.tftbuilder.models import Classe

def all_classes():
    classes = [
        {
            "nome":"Ascendente",
            "condicoes_ativacao": [1],
            "imagem": 'classes/ascendente.png'
        },
        {
            "nome":"Bastiao",
            "condicoes_ativacao": [2, 4, 6, 8],
            "imagem": 'classes/bastiao.png'
        },
        {
            "nome":"Rainha-morcego",
            "condicoes_ativacao": [1],
            "imagem": 'classes/rainha_morcego.png'
        },
        {
            "nome":"Melhores-amigos",
            "condicoes_ativacao": [1],
            "imagem": 'classes/melhores_amigos.png'
        },
        {
            "nome":"Detonador",
            "condicoes_ativacao": [2, 4, 6],
            "imagem": 'classes/detonador.png'
        },
        {
            "nome":"Caçador",
            "condicoes_ativacao": [2, 4, 6],
            "imagem": 'classes/cacador.png'
        },
        {
            "nome":"Mágico",
            "condicoes_ativacao": [2, 4],
            "imagem": 'classes/magico.png'
        },
        {
            "nome":"Mago",
            "condicoes_ativacao": [3, 5, 7, 9],
            "imagem": 'classes/mago.png'
        },
        {
            "nome":"Multiataque",
            "condicoes_ativacao": [3, 5, 7, 9],
            "imagem": 'classes/multiataque.png'
        },
        {
            "nome":"Preservador",
            "condicoes_ativacao": [2, 3, 4, 5],
            "imagem": 'classes/preservador.png'
        },
        {
            "nome":"Intelectual",
            "condicoes_ativacao": [2, 4, 6],
            "imagem": 'classes/intelectual.png'
        },
        {
            "nome":"Metamorfo",
            "condicoes_ativacao": [2, 4, 6, 8],
            "imagem": 'classes/metamorfo.png'
        },
        {
            "nome":"Vanguarda",
            "condicoes_ativacao": [2, 4, 6],
            "imagem": 'classes/vanguarda.png'
        },
        {
            "nome":"Guerreiro",
            "condicoes_ativacao": [2, 4, 6],
            "imagem": 'classes/guerreiro.png'
        },
        {
            "nome":"Arcana",
            "condicoes_ativacao": [2, 3, 4, 5],
            "imagem": 'classes/arcana.png'
        },
        {
            "nome":"Temporal",
            "condicoes_ativacao": [2, 4, 6],
            "imagem": 'classes/temporal.png'
        },
        {
            "nome":"Dragão",
            "condicoes_ativacao": [2, 3],
            "imagem": 'classes/dragao.png'
        },
        {
            "nome":"Druida",
            "condicoes_ativacao": [1],
            "imagem": 'classes/druida.png'
        },
        {
            "nome":"Macabro",
            "condicoes_ativacao": [3, 5, 7, 10],
            "imagem": 'classes/macabro.png'
        },
        {
            "nome":"Fada",
            "condicoes_ativacao": [2, 4, 6, 8],
            "imagem": 'classes/fada.png'
        },
        {
            "nome":"Congelado",
            "condicoes_ativacao": [3, 5, 7, 9],
            "imagem": 'classes/congelado.png'
        },
        {
            "nome":"Melmancia",
            "condicoes_ativacao": [3, 5, 7],
            "imagem": 'classes/melmancia.png'
        },
        {
            "nome":"Portal",
            "condicoes_ativacao": [3, 6, 8, 10],
            "imagem": 'classes/portal.png'
        },
        {
            "nome":"Pirofagia",
            "condicoes_ativacao": [2, 3, 4, 5],
            "imagem": 'classes/pirofagia.png'
        },
        {
            "nome":"Voraz",
            "condicoes_ativacao": [1],
            "imagem": 'classes/voraz.png'
        },
        {
            "nome":"Docemania",
            "condicoes_ativacao": [2, 4, 6],
            "imagem": 'classes/docemania.png'
        },
        {
            "nome":"Bruxaria",
            "condicoes_ativacao": [2, 4, 6, 8],
            "imagem": 'classes/bruxaria.png'
        },
    ]