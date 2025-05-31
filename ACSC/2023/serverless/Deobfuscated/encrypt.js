var a = document['querySelector']('form');
a['addEventListener']('submit', function(c) {
    c['preventDefault']();
    var d = document['querySelector']('textarea[name=\'message\']')['value'],
        e = document['querySelector']('input[name=\'password\']')['value'],
        f = document['querySelector']('input[name=\'encrypt\']'),
        g = b(d, e),
        h = document['querySelector']('p.response');
    h && h['remove']();
    var i = document['createElement']('p');
    i['classList']['add']('response'), i['textContent'] = 'Encrypted message: ' + g, f['insertAdjacentElement']('afterend', i);
});

function b(d, f) {
    var g = [0x9940435684b6dcfe5beebb6e03dc894e26d6ff83faa9ef1600f60a0a403880ee166f738dd52e3073d9091ddabeaaff27c899a5398f63c39858b57e734c4768b7n, 
             0xbd0d6bef9b5642416ffa04e642a73add5a9744388c5fbb8645233b916f7f7b89ecc92953c62bada039af19caf20ecfded79f62d99d86183f00765161fcd71577n, 
             0xa9fe0fe0b400cd8b58161efeeff5c93d8342f9844c8d53507c9f89533a4b95ae5f587d79085057224ca7863ea8e509e2628e0b56d75622e6eace59d3572305b9n, 
             0x8b7f4e4d82b59122c8b511e0113ce2103b5d40c549213e1ec2edba3984f4ece0346ab1f3f3c0b25d02c1b21d06e590f0186635263407e0b2fa16c0d0234e35a3n, 
             0xf840f1ee2734110a23e9f9e1a05b78eb711c2d782768cef68e729295587c4aa4af6060285d0a2c1c824d2c901e5e8a1b1123927fb537f61290580632ffea0fbbn, 
             0xdd068fd4984969a322c1c8adb4c8cc580adf6f5b180b2aaa6ec8e853a6428a219d7bffec3c3ec18c8444e869aa17ea9e65ed29e51ace4002cdba343367bf16fdn, 
             0x96e2cefe4c1441bec265963da4d10ceb46b7d814d5bc15cc44f17886a09390999b8635c8ffc7a943865ac67f9043f21ca8d5e4b4362c34e150a40af49b8a1699n, 
             0x81834f81b3b32860a6e7e741116a9c446ebe4ba9ba882029b7922754406b8a9e3425cad64bda48ae352cdc71a7d9b4b432f96f51a87305aebdf667bc8988d229n, 
             0xd8200af7c41ff37238f210dc8e3463bc7bcfb774be93c4cff0e127040f63a1bce5375de96b379c752106d3f67ec8dceca3ed7b69239cf7589db9220344718d5fn, 
             0xb704667b9d1212ae77d2eb8e3bd3d5a4cd19aa36fc39768be4fe0656c78444970f5fc14dc39a543d79dfe9063b30275033fc738116e213d4b6737707bb2fd287n],
        h = [0xd4aa1036d7d302d487e969c95d411142d8c6702e0c4b05e2fbbe274471bf02f8f375069d5d65ab9813f5208d9d7c11c11d55b19da1132c93eaaaba9ed7b3f9b1n, 
             0xc9e55bae9f5f48006c6c01b5963199899e1cdf364759d9ca5124f940437df36e8492b3c98c680b18cac2a847eddcb137699ffd12a2323c9bc74db2c720259a35n, 
             0xcbcdd32652a36142a02051c73c6d64661fbdf4cbae97c77a9ce1a41f74b45271d3200678756e134fe46532f978b8b1d53d104860b3e81bdcb175721ab222c611n, 
             0xf79dd7feae09ae73f55ea8aa40c49a7bc022c754db41f56466698881f265507144089af47d02665d31bba99b89e2f70dbafeba5e42bdac6ef7c2f22efa680a67n, 
             0xab50277036175bdd4e2c7e3b7091f482a0cce703dbffb215ae91c41742db6ed0d87fd706b622f138741c8b56be2e8bccf32b7989ca1383b3d838a49e1c28a087n, 
             0xb5e8c7706f6910dc4b588f8e3f3323503902c1344839f8fcc8d81bfa8e05fec2289af82d1dd19afe8c30e74837ad58658016190e070b845de4449ffb9a48b1a7n, 
             0xc351c7115ceffe554c456dcc9156bc74698c6e05d77051a6f2f04ebc5e54e4641fe949ea7ae5d5d437323b6a4be7d9832a94ad747e48ee1ebac9a70fe7cfec95n, 
             0x815f17d7cddb7618368d1e1cd999a6cb925c635771218d2a93a87a690a56f4e7b82324cac7651d3fbbf35746a1c787fa28ee8aa9f04b0ec326c1530e6dfe7569n, 
             0xe226576ef6e582e46969e29b5d9a9d11434c4fcfeccd181e7c5c1fd2dd9f3ff19641b9c5654c0f2d944a53d3dcfef032230c4adb788b8188314bf2ccf5126f49n, 
             0x84819ec46812a347894ff6ade71ae351e92e0bd0edfe1c87bda39e7d3f13fe54c51f94d0928a01335dd5b8689cb52b638f55ced38693f0964e78b212178ab397n],
        j = Math.floor(Math.random() * 10),
        k = Math.floor(Math.random() * 10),
        l = g[j],
        o = h[k],
        r = l * o,
        s = Math.floor(Math.random() * 5),
        t = Math.pow(2, Math.pow(2, s)) + 1;

    function u(A) {
        var B = new TextEncoder()['encode'](A);
        let C = 0x0n;
        for (let D = 0; D < B['length']; D++) {
            C = (C << 0x8n) + BigInt(B[D]);
        }
        return C;
    }
    var v = u(d);

    function w(A, B, C) {
        if (B === 0) return 0x1n;
        return B % 2 === 0 ? w(A * A % C, B / 2, C) : A * w(A, B - 1, C) % C;
    }
    var x = w(v, t, r);
    let y = [];
    while (x > 0) {
        y['push'](Number(x & 0xffn)), x = x >> 0x8n;
    }
    y['push'](Number(s)), y['push'](Number(k)), y['push'](Number(j));
    var z = new TextEncoder()['encode'](f);
    for (let A = 0; A < y['length']; ++A) {
        y[A] = y[A] ^ z[A % z['length']];
    }
    return btoa(y['reverse']());
}