FERMATUM_VERSION = '2.8.2'  # version of the client package
PROTOCOL_VERSION = '0.10'   # protocol version requested

# The hash of the mnemonic seed must begin with this
SEED_PREFIX      = '01'      # Fermatum standard wallet
SEED_PREFIX_SW   = '02'      # Fermatum segwit wallet
SEED_PREFIX_2FA  = '101'     # extended seed for two-factor authentication


def seed_prefix(seed_type):
    if seed_type == 'standard':
        return SEED_PREFIX
    elif seed_type == 'segwit':
        return SEED_PREFIX_SW
    elif seed_type == '2fa':
        return SEED_PREFIX_2FA
