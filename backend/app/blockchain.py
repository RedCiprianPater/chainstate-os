class BlockchainVerifier:
    """Fail-closed adapter. Implement with a vetted provider before enabling payments."""

    def verify_native_eth_payment(self, *, tx_hash: str, expected_chain_id: int,
                                  expected_recipient: str, expected_amount_wei: str,
                                  payer_wallet: str, required_confirmations: int) -> bool:
        # Deliberately denies all requests until a production implementation exists.
        return False

    def recover_and_verify_signature(self, *, message: str, signature: str,
                                     expected_wallet: str) -> bool:
        # Implement EIP-712 typed-data verification with a vetted library.
        return False


verifier = BlockchainVerifier()
