
#Note that Optimism, Moonbeam, and Boba are all on public rpcs and not omnirpc
chains = {
    'arbitrum': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/42161', 'bridge': '0x6F4e8eBa4D337f874Ab57478AcC2Cb5BACdc19c9', 'minichef': '0x73186f2Cf2493f20836b17b21ae79fc12934E207', 'syn': '0x080f6aed32fc474dd5717105dba5ea57268f46eb',  'cctp': '0x49357ba0Ef3a8daC25903472eEe45C41221D4F9a'},
    'aurora': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/1313161554', 'bridge': '0xaeD5b25BE1c3163c907a471082640450F928DDFE', 'minichef': '0x809DC529f07651bD43A172e8dB6f4a7a0d771036', 'syn': '0xd80d8688b02B3FD3afb81cDb124F188BB5aD0445',  'cctp': ''},
    'avalanche': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/43114', 'bridge': '0xC05e61d0E7a63D27546389B7aD62FdFf5A91aACE', 'minichef': '0x3a01521F8E7F012eB37eAAf1cb9490a5d9e18249', 'syn': '0x1f1E7c893855525b303f99bDF5c3c05Be09ca251',  'cctp': '0x49357ba0Ef3a8daC25903472eEe45C41221D4F9a'},
    'base': {'url': 'https://developer-access-mainnet.base.org', 'bridge': '0xf07d1C752fAb503E47FEF309bf14fbDD3E867089', 'minichef': '0xfFC2d603fde1F99ad94026c00B6204Bb9b8c36E9', 'syn': '0x432036208d2717394d2614d6697c46DF3Ed69540',  'cctp': '0x49357ba0Ef3a8daC25903472eEe45C41221D4F9a'},
    'blast': {'url': 'https://rpc.blast.io', 'bridge': '0x55769bAF6ec39B3bf4aAE948eB890eA33307Ef3C', 'minichef': '0x3100dC8464A8523306c3C5034de24a8927d6E590', 'syn': '0x9592f08387134e218327E6E8423400eb845EdE0E',  'cctp': ''},
    'boba': {'url': 'https://mainnet.boba.network', 'bridge': '0x432036208d2717394d2614d6697c46DF3Ed69540', 'minichef': '0xd5609cD0e1675331E4Fb1d43207C8d9D83AAb17C', 'syn': '0xb554A55358fF0382Fb21F0a478C3546d1106Be8c',  'cctp': ''},
    'bsc': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/56', 'bridge': '0xd123f70AE324d34A9E76b67a27bf77593bA8749f', 'minichef': '0x8F5BBB2BB8c2Ee94639E55d5F41de9b4839C1280', 'syn': '0xa4080f1778e69467e905b8d6f72f6e441f9e9484',  'cctp': ''},
    'canto': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/7700', 'bridge': '0xDde5BEC4815E1CeCf336fb973Ca578e8D83606E0', 'minichef': '0x93124c923dA389Bc0f13840fB822Ce715ca67ED6', 'syn': '0x555982d2E211745b96736665e19D9308B615F78e',  'cctp': ''},
    'cronos': {'url': 'https://cronos-evm.publicnode.com', 'bridge': '0xE27BFf97CE92C3e1Ff7AA9f86781FDd6D48F5eE9', 'minichef': '', 'syn': '0xFD0F80899983b8D46152aa1717D76cba71a31616',  'cctp': ''},
    'dfk': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/53935', 'bridge': '0xE05c976d3f045D0E6E7A6f61083d98A15603cF6A', 'minichef': '', 'syn': '0xB6b5C854a8f71939556d4f3a2e5829F7FcC1bf2A',  'cctp': ''},
    'dogechain': {'url': 'https://rpc.dogechain.dog', 'bridge': '0x9508BF380c1e6f751D97604732eF1Bae6673f299', 'minichef': '0x995Abc3EEf2894E8923E1d58e5E62f2BCF90cd4E', 'syn': '0xDfA53EeBA61D69E1D2b56b36d78449368F0265c1',  'cctp': ''},
    'ethereum': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/1', 'bridge': '0x2796317b0fF8538F253012862c06787Adfb8cEb6', 'minichef': '0xd10eF2A513cEE0Db54E959eF16cAc711470B62cF', 'syn': '0x0f2D719407FdBeFF09D87557AbB7232601FD9F29',  'cctp': '0x49357ba0Ef3a8daC25903472eEe45C41221D4F9a'},
    'fantom': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/250', 'bridge': '0xAf41a65F786339e7911F4acDAD6BD49426F2Dc6b', 'minichef': '0xaeD5b25BE1c3163c907a471082640450F928DDFE', 'syn': '0xE55e19Fb4F2D85af758950957714292DAC1e25B2',  'cctp': ''},
    'harmony': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/1666600000', 'bridge': '0xAf41a65F786339e7911F4acDAD6BD49426F2Dc6b', 'minichef': '0xaeD5b25BE1c3163c907a471082640450F928DDFE', 'syn': '0xE55e19Fb4F2D85af758950957714292DAC1e25B2',  'cctp': ''},
    'klaytn': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/8217', 'bridge': '0xAf41a65F786339e7911F4acDAD6BD49426F2Dc6b', 'minichef': '0xF68cD56cF9a9e1cDa181fb2C44C5F0E98B5cC541', 'syn': '0xF5f3650f54dA85e4A4D8E490139C77275B167c53',  'cctp': ''},
    'metis': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/1088', 'bridge': '0x06Fea8513FF03a0d3f61324da709D4cf06F42A5c', 'minichef': '0xaB0D8Fc46249DaAcd5cB36c5F0bC4f0DAF34EBf5', 'syn': '0x67c10c397dd0ba417329543c1a40eb48aaa7cd00',  'cctp': ''},
    'moonriver': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/1285', 'bridge': '0xaeD5b25BE1c3163c907a471082640450F928DDFE', 'minichef': '', 'syn': '0xd80d8688b02B3FD3afb81cDb124F188BB5aD0445',  'cctp': ''},
    'moonbeam': {'url': 'https://rpc.api.moonbeam.network', 'bridge': '0x84A420459cd31C3c34583F67E0f0fB191067D32f', 'minichef': '', 'syn': '0xF44938b0125A6662f9536281aD2CD6c499F22004',  'cctp': ''},
    'optimism': {'url': 'https://mainnet.optimism.io', 'bridge': '0xAf41a65F786339e7911F4acDAD6BD49426F2Dc6b', 'minichef': '0xe8c610fcb63A4974F02Da52f0B4523937012Aaa0', 'syn': '0x5A5fFf6F753d7C11A56A52FE47a177a87e431655',  'cctp':'0x49357ba0Ef3a8daC25903472eEe45C41221D4F9a'},
    'polygon': {'url': 'https://rpc.omnirpc.io/confirmations/1/rpc/137', 'bridge': '0x8F5BBB2BB8c2Ee94639E55d5F41de9b4839C1280', 'minichef': '0x7875Af1a6878bdA1C129a4e2356A3fD040418Be5', 'syn': '0xf8f9efc0db77d8881500bb06ff5d6abc3070e695',  'cctp': '0x49357ba0Ef3a8daC25903472eEe45C41221D4F9a'}
}



#need to add canto and metis