from app import app


def test_rota_saude_retorna_status_e_versao():
    resposta = app.test_client().get("/saude")

    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados["status"] == "ok"
    assert "versao" in dados
