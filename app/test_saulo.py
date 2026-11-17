from app import app


def test_rota_inexistente_retorna_404():
    resposta = app.test_client().get("/nao-existe")

    assert resposta.status_code == 404
