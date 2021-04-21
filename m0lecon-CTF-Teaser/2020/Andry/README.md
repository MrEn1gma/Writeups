# Author: @madt1m
# Challenge file: andry.apk
# Description:
> So, I am developing this app to store my secret flag in a weird way. It's not complete though... but you have your tools to overcome that, right?

# Introduction
> Well, today is a perfect day to find a new techniques and i chose m0leCon to practice reversing Android :D. In this challenge, i took about 30 mins to complete. :"))))))))))
> 
> OK, lets work.

I hate install Android Studio, because of lag when i started with Visual Studio Code, so i decided to use `decompiler.com`, we can view the result after decompiled successful:

I'll choose `OnCreate()` and call it's main function.
```java
    /* access modifiers changed from: protected */
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView((int) R.layout.activity_main);
        ((Button) findViewById(R.id.button2)).setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                if (MainActivity.this.check_password().booleanValue()) {
                    Toast.makeText(MainActivity.this.getApplicationContext(), "Yes!", 0).show();
                    DynamicLoaderService.startActionLoad(MainActivity.this.getApplicationContext(), ((EditText) MainActivity.this.findViewById(R.id.editPassword1)).getText().toString());
                    return;
                }
                Toast.makeText(MainActivity.this.getApplicationContext(), "No...", 0).show();
            }
        });
    }
```
