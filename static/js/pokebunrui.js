const point = document.getElementById('point');
let pointCount = Number(localStorage.getItem('pointMemory'));
        let answer = document.getElementById('answer');
        const btn = document.getElementById('btn');
        const hint = document.getElementById('hint');
        const hint1Text = document.getElementById('hint1_text');
        const hint2Text = document.getElementById('hint2_text');

        const pokeName = document.getElementById('poke_name');
        const torf = document.getElementById('status');
        const seeAnswer = document.getElementById('see_answer');
        const img = document.getElementById('img');
        const zukan = document.getElementById('zukan');
        const reset = document.getElementById('reset');
        const otherAns = document.getElementById('other_ans')

        let hintCounter = 0;


        function openAllHints() {
            hint1Text.style.display = 'block';
            hint2Text.style.display = 'block';
            hint.disabled = true;
            otherAns.style.display = 'block';
        }
        
        btn.addEventListener('click', () => {
            console.log(answer.value);
            if (pokeName.innerText.includes(answer.value) || otherAns.innerText.includes(answer.value)) {
                torf.innerText = '正解';
                torf.style.color = '#ff0000';
                pointCount += 5;
                localStorage.setItem("pointMemory", pointCount);
                point.innerText = localStorage.getItem('pointMemory');
                openAllHints();
            } else {
                torf.innerText = '不正解';
                torf.style.color = 'blue';
                pointCount -= 1;
                localStorage.setItem("pointMemory", pointCount);
                point.innerText = localStorage.getItem('pointMemory');
            }
        });

        hint.addEventListener('click', () => {
            if (hintCounter == 0) {
                hint1Text.style.display = 'block';
                hint.innerHTML = 'ヒント2を見る';
                pointCount -= 1;
                localStorage.setItem("pointMemory", pointCount);
                point.innerText = localStorage.getItem('pointMemory');
                hintCounter += 1;
            } else {
                hint2Text.style.display = 'block';
                pointCount -= 1;
                localStorage.setItem("pointMemory", pointCount);
                point.innerText = localStorage.getItem('pointMemory');
                hint.disabled = true;
                hintCounter += 1;
            }
                
        });

        seeAnswer.addEventListener('click', () => {
            pokeName.style.display = 'block';
            img.style.display = 'block';
            zukan.style.display = 'block';
            btn.disabled = true;
            openAllHints();

        });

        reset.addEventListener('click', () => {
            let result = window.confirm('リセットしますか？')
            if (result) {
                localStorage.removeItem("pointMemory", pointCount)
                point.innerText = 0;
                location.reload();
            }
                
        })

        window.addEventListener('load', () => {
            if (localStorage.getItem('pointMemory')) {
                point.innerText = localStorage.getItem('pointMemory');
            }else {
                point.innerText = 0;
            }

        })