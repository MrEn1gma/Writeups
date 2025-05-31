use std::io::{self, Read};
use aes::Aes256;
use aes::cipher::generic_array::GenericArray;
use aes::cipher::{BlockEncrypt, KeyInit};
use nuts_and_bolts::StorageMethod;
use rand::Rng;


fn main() {
    let mut flag = [0u8; 64];                                   // flag 64 bytes
    io::stdin().read(&mut flag).expect("Flag not provided");
    
    let orig_key = rand::thread_rng().gen::<[u8; 32]>();        
    let key = GenericArray::from(orig_key);                     // key generated random with length 32 bytes
    let cipher = Aes256::new(&key);                             // AES 256 bits with mode ECB

    flag.chunks_mut(16).for_each(|block| {
        cipher.encrypt_block(GenericArray::from_mut_slice(block)); // Run time per 16 byte block in mode ECB
    });
    let mut key = StorageMethod::plain(orig_key);
    let mut flag = StorageMethod::plain(flag);
    let mut rng = rand::thread_rng();                           // gen
    for _ in 0..10 {
        key = if rng.gen::<u8>() % 2 == 0 {                     // key always is 13
            key.reverse()
        } else {
            key.xor()                                           // xor_key ^ key[i]
        };
        flag = if rng.gen::<u8>() % 2 == 0 {
            flag.reverse()
        } else {
            flag.xor()
        };
    }
    println!("Here's your key: {:?}!", bincode::serialize(&key).unwrap());
    println!("And here's your flag: {:?}!", bincode::serialize(&flag).unwrap());
}

