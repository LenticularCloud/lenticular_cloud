from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JSONWebKey")


@attr.s(auto_attribs=True)
class JSONWebKey:
    """It is important that this model object is named JSONWebKey for
    "swagger generate spec" to generate only on definition of a
    JSONWebKey.

        Attributes:
            alg (str): The "alg" (algorithm) parameter identifies the algorithm intended for
                use with the key.  The values used should either be registered in the
                IANA "JSON Web Signature and Encryption Algorithms" registry
                established by [JWA] or be a value that contains a Collision-
                Resistant Name. Example: RS256.
            kid (str): The "kid" (key ID) parameter is used to match a specific key.  This
                is used, for instance, to choose among a set of keys within a JWK Set
                during key rollover.  The structure of the "kid" value is
                unspecified.  When "kid" values are used within a JWK Set, different
                keys within the JWK Set SHOULD use distinct "kid" values.  (One
                example in which different keys might use the same "kid" value is if
                they have different "kty" (key type) values but are considered to be
                equivalent alternatives by the application using them.)  The "kid"
                value is a case-sensitive string. Example: 1603dfe0af8f4596.
            kty (str): The "kty" (key type) parameter identifies the cryptographic algorithm
                family used with the key, such as "RSA" or "EC". "kty" values should
                either be registered in the IANA "JSON Web Key Types" registry
                established by [JWA] or be a value that contains a Collision-
                Resistant Name.  The "kty" value is a case-sensitive string. Example: RSA.
            use (str): Use ("public key use") identifies the intended use of
                the public key. The "use" parameter is employed to indicate whether
                a public key is used for encrypting data or verifying the signature
                on data. Values are commonly "sig" (signature) or "enc" (encryption). Example: sig.
            crv (Union[Unset, str]):  Example: P-256.
            d (Union[Unset, str]):  Example:
                T_N8I-6He3M8a7X1vWt6TGIx4xB_GP3Mb4SsZSA4v-orvJzzRiQhLlRR81naWYxfQAYt5isDI6_C2L9bdWo4FFPjGQFvNoRX-_sBJyBI_rl-
                TBgsZYoUlAj3J92WmY2inbA-PwyJfsaIIDceYBC-eX-
                xiCu6qMqkZi3MwQAFL6bMdPEM0z4JBcwFT3VdiWAIRUuACWQwrXMq672x7fMuaIaHi7XDGgt1ith23CLfaREmJku9PQcchbt_uEY-hqrFY6ntTtS
                4paWWQj86xLL94S-Tf6v6xkL918PfLSOTq6XCzxvlFwzBJqApnAhbwqLjpPhgUG04EDRrqrSBc5Y1BLevn6Ip5h1AhessBp3wLkQgz_roeckt-
                ybvzKTjESMuagnpqLvOT7Y9veIug2MwPJZI2VjczRc1vzMs25XrFQ8DpUy-bNdp89TmvAXwctUMiJdgHloJw23Cv03gIUAkDnsTqZmkpbIf-crpg
                NKFmQP_EDKoe8p_PXZZgfbRri3NoEVGP7Mk6yEu8LjJhClhZaBNjuWw2-KlBfOA3g79mhfBnkInee5KO9mGR50qPk1V-MorUYNTFMZIm0kFE6eYV
                WFBwJHLKYhHU34DoiK1VP-svZpC2uAMFNA_UJEwM9CQ2b8qe4-5e9aywMvwcuArRkAB5mBIfOaOJao3mfukKAE.
            dp (Union[Unset, str]):  Example: G4sPXkc6Ya9y8oJW9_ILj4xuppu0lzi_H7VTkS8xj5SdX3coE0oimYwxIi2emTAue0UOa5dpgFGyBJ
                4c8tQ2VF402XRugKDTP8akYhFo5tAA77Qe_NmtuYZc3C3m3I24G2GvR5sSDxUyAN2zq8Lfn9EUms6rY3Ob8YeiKkTiBj0.
            dq (Union[Unset, str]):  Example: s9lAH9fggBsoFR8Oac2R_E2gw282rT2kGOAhvIllETE1efrA6huUUvMfBcMpn8lqeW6vzznYY5SSQF
                7pMdC_agI3nG8Ibp1BUb0JUiraRNqUfLhcQb_d9GF4Dh7e74WbRsobRonujTYN1xCaP6TO61jvWrX-L18txXw494Q_cgk.
            e (Union[Unset, str]):  Example: AQAB.
            k (Union[Unset, str]):  Example: GawgguFyGrWKav7AX4VKUg.
            n (Union[Unset, str]):  Example: vTqrxUyQPl_20aqf5kXHwDZrel-KovIp8s7ewJod2EXHl8tWlRB3_Rem34KwBfqlKQGp1nqah-51H4J
                zruqe0cFP58hPEIt6WqrvnmJCXxnNuIB53iX_uUUXXHDHBeaPCSRoNJzNysjoJ30TIUsKBiirhBa7f235PXbKiHducLevV6PcKxJ5cY8zO286qJL
                BWSPm-OIevwqsIsSIH44Qtm9sioFikhkbLwoqwWORGAY0nl6XvVOlhADdLjBSqSAeT1FPuCDCnXwzCDR8N9IFB_IjdStFkC-rVt2K5BYfPd0c3yF
                p_vHR15eRd0zJ8XQ7woBC8Vnsac6Et1pKS59pX6256DPWu8UDdEOolKAPgcd_g2NpA76cAaF_jcT80j9KrEzw8Tv0nJBGesuCjPNjGs_KzdkWTUX
                t23Hn9QJsdc1MZuaW0iqXBepHYfYoqNelzVte117t4BwVp0kUM6we0IqyXClaZgOI8S-WDBw2_Ovdm8e5NmhYAblEVoygcX8Y46oH6bKiaCQfKCF
                DMcRgChme7AoE1yZZYsPbaG_3IjPrC4LBMHQw8rM9dWjJ8ImjicvZ1pAm0dx-
                KHCP3y5PVKrxBDf1zSOsBRkOSjB8TPODnJMz6-jd5hTtZxpZPwPoIdCanTZ3ZD6uRBpTmDwtpRGm63UQs1m5FWPwb0T2IF0.
            p (Union[Unset, str]):  Example: 6NbkXwDWUhi-eR55Cgbf27FkQDDWIamOaDr0rj1q0f1fFEz1W5A_09YvG09Fiv1AO2-D8Rl8gS1Vkz2
                i0zCSqnyy8A025XOcRviOMK7nIxE4OH_PEsko8dtIrb3TmE2hUXvCkmzw9EsTF1LQBOGC6iusLTXepIC1x9ukCKFZQvdgtEObQ5kzd9Nhq-cdqmS
                eMVLoxPLd1blviVT9Vm8-y12CtYpeJHOaIDtVPLlBhJiBoPKWg3vxSm4XxIliNOefqegIlsmTIa3MpS6WWlCK3yHhat0Q-rRxDxdyiVdG_wzJvp0
                Iw_2wms7pe-PgNPYvUWH9JphWP5K38YqEBiJFXQ.
            q (Union[Unset, str]):  Example: 0A1FmpOWR91_RAWpqreWSavNaZb9nXeKiBo0DQGBz32DbqKqQ8S4aBJmbRhJcctjCLjain-
                ivut477tAUMmzJwVJDDq2MZFwC9Q-4VYZmFU4HJityQuSzHYe64RjN-E_NQ02TWhG3QGW6roq6c57c99rrUsETwJJiwS8M5p15Miuz53DaOjv-
                uqqFAFfywN5WkxHbraBcjHtMiQuyQbQqkCFh-oanHkwYNeytsNhTu2mQmwR5DR2roZ2nPiFjC6nsdk-A7E3S3wMzYYFw7jvbWWoYWo9vB40_MY2Y
                0FYQSqcDzcBIcq_0tnnasf3VW4Fdx6m80RzOb2Fsnln7vKXAQ.
            qi (Union[Unset, str]):  Example: GyM_p6JrXySiz1toFgKbWV-JdI3jQ4ypu9rbMWx3rQJBfmt0FoYzgUIZEVFEcOqwemRN81zoDAaa-
                Bk0KWNGDjJHZDdDmFhW3AN7lI-puxk_mHZGJ11rxyR8O55XLSe3SPmRfKwZI6yU24ZxvQKFYItdldUKGzO6Ia6zTKhAVRU.
            x (Union[Unset, str]):  Example: f83OJ3D2xF1Bg8vub9tLe1gHMzV76e8Tus9uPHvRVEU.
            x5c (Union[Unset, List[str]]): The "x5c" (X.509 certificate chain) parameter contains a chain of one
                or more PKIX certificates [RFC5280].  The certificate chain is
                represented as a JSON array of certificate value strings.  Each
                string in the array is a base64-encoded (Section 4 of [RFC4648] --
                not base64url-encoded) DER [ITU.X690.1994] PKIX certificate value.
                The PKIX certificate containing the key value MUST be the first
                certificate.
            y (Union[Unset, str]):  Example: x_FEzRu9m36HLN_tue659LNpXW6pCyStikYjKIWI5a0.
    """

    alg: str
    kid: str
    kty: str
    use: str
    crv: Union[Unset, str] = UNSET
    d: Union[Unset, str] = UNSET
    dp: Union[Unset, str] = UNSET
    dq: Union[Unset, str] = UNSET
    e: Union[Unset, str] = UNSET
    k: Union[Unset, str] = UNSET
    n: Union[Unset, str] = UNSET
    p: Union[Unset, str] = UNSET
    q: Union[Unset, str] = UNSET
    qi: Union[Unset, str] = UNSET
    x: Union[Unset, str] = UNSET
    x5c: Union[Unset, List[str]] = UNSET
    y: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alg = self.alg
        kid = self.kid
        kty = self.kty
        use = self.use
        crv = self.crv
        d = self.d
        dp = self.dp
        dq = self.dq
        e = self.e
        k = self.k
        n = self.n
        p = self.p
        q = self.q
        qi = self.qi
        x = self.x
        x5c: Union[Unset, List[str]] = UNSET
        if not isinstance(self.x5c, Unset):
            x5c = self.x5c

        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alg": alg,
                "kid": kid,
                "kty": kty,
                "use": use,
            }
        )
        if crv is not UNSET:
            field_dict["crv"] = crv
        if d is not UNSET:
            field_dict["d"] = d
        if dp is not UNSET:
            field_dict["dp"] = dp
        if dq is not UNSET:
            field_dict["dq"] = dq
        if e is not UNSET:
            field_dict["e"] = e
        if k is not UNSET:
            field_dict["k"] = k
        if n is not UNSET:
            field_dict["n"] = n
        if p is not UNSET:
            field_dict["p"] = p
        if q is not UNSET:
            field_dict["q"] = q
        if qi is not UNSET:
            field_dict["qi"] = qi
        if x is not UNSET:
            field_dict["x"] = x
        if x5c is not UNSET:
            field_dict["x5c"] = x5c
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        alg = _d.pop("alg")

        kid = _d.pop("kid")

        kty = _d.pop("kty")

        use = _d.pop("use")

        crv = _d.pop("crv", UNSET)

        d = _d.pop("d", UNSET)

        dp = _d.pop("dp", UNSET)

        dq = _d.pop("dq", UNSET)

        e = _d.pop("e", UNSET)

        k = _d.pop("k", UNSET)

        n = _d.pop("n", UNSET)

        p = _d.pop("p", UNSET)

        q = _d.pop("q", UNSET)

        qi = _d.pop("qi", UNSET)

        x = _d.pop("x", UNSET)

        x5c = cast(List[str], _d.pop("x5c", UNSET))

        y = _d.pop("y", UNSET)

        json_web_key = cls(
            alg=alg,
            kid=kid,
            kty=kty,
            use=use,
            crv=crv,
            d=d,
            dp=dp,
            dq=dq,
            e=e,
            k=k,
            n=n,
            p=p,
            q=q,
            qi=qi,
            x=x,
            x5c=x5c,
            y=y,
        )

        json_web_key.additional_properties = _d
        return json_web_key

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
