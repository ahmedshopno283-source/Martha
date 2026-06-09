<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Select Your Character</title>
    <!-- টেলিগ্রামের অফিশিয়াল মিনি অ্যাপ স্ক্রিপ্ট (এটি ছাড়া ডাটা ট্রান্সফার হবে না) -->
    <script src="https://telegram.org"></script>
    <style>
        body { font-family: Arial, sans-serif; background-color: #1e1e2e; color: white; text-align: center; padding: 20px; margin: 0; }
        h2 { color: #ff477e; margin-top: 10px; }
        .container { display: flex; flex-direction: column; gap: 15px; margin-top: 20px; }
        .card { background: #2b2b3a; padding: 18px; border-radius: 12px; border: 1px solid #ff477e; cursor: pointer; transition: 0.3s; -webkit-tap-highlight-color: transparent; }
        .card:hover, .card:active { background: #ff477e; transform: scale(1.02); }
        .name { font-size: 18px; font-weight: bold; margin-bottom: 5px; }
        .desc { font-size: 13px; color: #ccc; }
    </style>
</head>
<body>

    <h2>তোমার ক্যারেক্টার বেছে নাও 🥰</h2>
    <p>কার সাথে ঘনিষ্ঠ সময় কাটাবে সোনা?</p>

    <div class="container">
        <!-- মায়া ক্যারেক্টার -->
        <div class="card" onclick="selectChar('মায়া (Maya)')">
            <div class="name">👩‍🦰 মায়া (Maya)</div>
            <div class="desc">মিষ্টি, লাজুক এবং ভীষণ রোম্যান্টিক স্বভাবের মেয়ে। ❤️</div>
        </div>

        <!-- নোভา ক্যারেক্টার -->
        <div class="card" onclick="selectChar('নোভา (Nova)')">
            <div class="name">👧 নোভা (Nova)</div>
            <div class="desc">বেশ চঞ্চল, আধুনিক এবং চরম ফ্লার্টিং করতে ওস্তাদ! 😉</div>
        </div>

        <!-- আরিয়া ক্যারেক্টার -->
        <div class="card" onclick="selectChar('আরিয়া (Aria)')">
            <div class="name">👩 আরিয়া (Aria)</div>
            <div class="desc">শান্ত প্রকৃতির কিন্তু তোমার প্রতি ভীষণ যত্নশীল ও কেয়ারিং। 💕</div>
        </div>
    </div>

    <script>
        // টেলিগ্রাম ওয়েব অ্যাপ ইনিশিয়ালাইজ করা
  
        // ১. আগে টেলিগ্রাম ওয়েব অ্যাপ ইনিশিয়ালাইজ করতে হবে (সঠিক ক্রম)
        const tg = window.Telegram.WebApp;
        tg.ready();
        tg.expand(); // অ্যাপটিকে পুরো স্ক্রিনে বড় করবে

        // ২. এরপর ফাংশনটি কাজ করবে
        function selectChar(characterName) {
            try {
                // এই স্পেশাল ফাংশনটি টেলিগ্রাম বটের চ্যাটে ডাটা পাঠিয়ে দেবে
                tg.sendData(characterName); 
            } catch (error) {
                alert("টেলিগ্রাম কানেকশন এরর: " + error);
            }
        }
    </script>   
    </script>
</body>
</html>
