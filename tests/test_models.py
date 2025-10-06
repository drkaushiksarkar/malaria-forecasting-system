from src.models.vae import CondVAE
def test_vae_instantiates():
    m = CondVAE()
    assert m is not None