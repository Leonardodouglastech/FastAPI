from fastapi import FastAPI


bancoDados = {
    "1":{
        "nome":"Pizza",
        "preco":"59,90"

},
    "2":{
        "nome":"Lasanha",
        "preco":"10"
    }
}
app = FastAPI()


# rota principal de apresentação
@app.get("/")
def apresentacao():
    return {
        "mensagem": "Olá Mundo",
        "statusCode": 200
    }
@app.get("/{nome}")
def saudacoes(nome):
    return {
        "mensagem":f"olá {nome}",
        "statusCode": 200
    }
@app.get("/produtos/")
def mostrarTodosProdutos():
    return bancoDados

@app.get("/produtos/{idProduto}")
def mostrarUmproduto(idProduto):
  try:
      if bancoDados[idProduto]:
          return {
              "produto": bancoDados[idProduto],
              "statusCode": 200
          }
  except:
      return{
          "produto":"não encontrado",
          "status": 404
      }
