from flask_talisman import Talisman
from flask_cors import CORS

CORS(app)

Talisman(
    app,
    content_security_policy=None,
    force_https=False
)