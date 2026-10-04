from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "chainstate-payment-backend"
    app_env: str = "development"
    host: str = "127.0.0.1"
    port: int = 8000
    database_url: str = "sqlite:///./chainstate.db"
    jwt_secret: str = ""
    admin_api_key: str = ""
    payment_asset: str = "ETH"
    payment_price_usd: int = 666
    payment_chain_id: int = 1
    payment_recipient_address: str = ""
    quote_ttl_seconds: int = 900
    required_confirmations: int = 12
    min_payment_wei: str = ""
    allowed_bundle_sha256: str = ""
    release_version: str = ""
    install_challenge_ttl_seconds: int = 300
    enable_live_payments: bool = False
    enable_install_authorization: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
