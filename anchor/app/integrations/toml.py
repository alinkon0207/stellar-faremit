from rest_framework.request import Request
from polaris.models import Asset

def toml_contents(request, *args, **kwargs): 
  asset = Asset.objects.first()
  # asset2 = Asset.objects.last()

  return {
    "DOCUMENTATION":
      {
        "ORG_NAME": "",
        "ORG_DBA": "",
        "ORG_URL": "",
        "ORG_LOGO": "",
        "ORG_DESCRIPTION": "",
        "ORG_PHYSICAL_ADDRESS": "",
        "ORG_TWITTER": "",
        "ORG_OFFICIAL_EMAIL": "",
        "ORG_GITHUB": "",
      },
    "PRINCIPALS": [
      {
        "name": "Edward Wolf",
        "email": "ewolf655@gmail.com"
      },
    ],
    "CURRENCIES": [
      {
        "code": asset.code,
        "issuer": asset.issuer,
        "name": "USD",
        "desc": "The official currency of the United States of America",
        "display_decimals": 2,
        "is_asset_anchored": "true",
        "is_unlimited": "true",
        "anchor_asset_type": "fiat",
        "anchor_asset": "USD",
        "redemption_instructions": "Access through trusted partners and stellar wallets",
        "status": "test",
        "image": "https://ipfs.io/ipfs/bafkreibpzncuhbk5ozhdw7xkcdoyf3xhwhcwcf6sj7axjzimxw6vm6pvyy"
      },
      # {
      #   "code": asset2.code,
      #   "issuer": asset2.issuer,
      #   "name": "USD Coin",
      #   "display_decimals": 2,
      #   "is_asset_anchored": "true",
      #   "is_unlimited": "true",
      #   "anchor_asset_type": "fiat",
      #   "anchor_asset": "USD",
      #   "status": "test",
      # }
    ]
  }
