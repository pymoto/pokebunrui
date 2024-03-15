const gameStartBtn = document.getElementById('game-start-btn');
const gameStartBtnWrapper = document.getElementById('game-start-btn-wrapper');

const pokebunrui10Main = document.getElementById('pokebunrui10-main');

const numberOfQuizzes = document.getElementById('number_of_quizzes');
const point = document.getElementById('point');
let nowPointCount = Number(localStorage.getItem('nowPoint'));
let quizOrder = Number(localStorage.getItem('nowQuizOrder'));
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
const nextQuiz = document.getElementById('next_quiz');
const reset = document.getElementById('reset');
const otherAns = document.getElementById('other_ans')
const otherAnswers = document.getElementById('other_answers')
const zukanFrame = document.getElementById('zukan_frame');
const startbtn = document.getElementById('startbtn');

let totalPointInput =document.getElementById('total-point-input');
const finishGameBtn = document.getElementById('finish-game-btn');
const newGame = document.getElementById('new-game');

const resetBtn = document.getElementById('reset-btn');




let hintCounter = 0;      


gameStartBtn.addEventListener('click', () => {
    pokebunrui10Main.style.display = 'block';
    gameStartBtnWrapper.style.display = 'none';
    localStorage.removeItem("nowPoint", nowPointCount);
    localStorage.removeItem('nowQuizOrder', quizOrder);
    quizOrder = 1;
    numberOfQuizzes.innerText = quizOrder + '問目';
    localStorage.setItem('nowQuizOrder', quizOrder);
    
})




function openAllHints() {
    hint1Text.style.display = 'block';
    hint2Text.style.display = 'block';
    hint.disabled = true;
    otherAnswers.style.display = 'block';
}

function finishQuiz() {
    pokeName.style.display = 'block';
    img.style.display = 'block';
    zukan.style.display = 'block';
    btn.disabled = true;
    quizOrder ++;
    localStorage.setItem('nowQuizOrder', quizOrder)
    if (localStorage.getItem('nowQuizOrder') != 11) {
        nextQuiz.disabled = false;
    }
    finishGameBtn.disabled = false;
}

const ansPokeArray = otherAns.textContent.split('・');

// startbtn.addEventListener('click', () => {
//     answer.disabled = false;
// })

btn.addEventListener('click', () => {

    if (answer.value != 'なし' && (answer.value == pokeName.textContent || ansPokeArray.includes(answer.value))) {
        torf.innerText = '正解';
        torf.style.color = '#ff0000';
        nowPointCount += 3;
        localStorage.setItem("nowPoint", nowPointCount);
        point.innerText = localStorage.getItem('nowPoint');
        finishQuiz();
        openAllHints();
    } else if (!answer.value || answer.value.includes('　')) {

    } else {
        torf.innerText = '不正解';
        torf.style.color = 'blue';
        nowPointCount -= 1;
        localStorage.setItem("nowPoint", nowPointCount);
        point.innerText = localStorage.getItem('nowPoint');
    } 
});

hint.addEventListener('click', () => {
    if (hintCounter == 0) {
        hint1Text.style.display = 'block';
        hint.innerHTML = 'ヒント2を見る';
        nowPointCount -= 1;
        localStorage.setItem("nowPoint", nowPointCount);
        point.innerText = localStorage.getItem('nowPoint');
        hintCounter += 1;
    } else {
        hint2Text.style.display = 'block';
        nowPointCount -= 1;
        localStorage.setItem("nowPoint", nowPointCount);
        point.innerText = localStorage.getItem('nowPoint');
        hint.disabled = true;
        hintCounter += 1;
    }
        
});

seeAnswer.addEventListener('click', () => {
    finishQuiz();
    openAllHints();
    
});

nextQuiz.addEventListener('click', () => {
    window.location.reload();
});




window.addEventListener('load', () => {

    if (localStorage.getItem('nowQuizOrder')) {
        
        
    }else {
        let quizOrder = 1;
        localStorage.setItem('nowQuizOrder', quizOrder);
        pokebunrui10Main.style.display = 'none';
        gameStartBtnWrapper.style.display = 'block';
    }

    numberOfQuizzes.innerText = quizOrder + '問目';
    
    if (localStorage.getItem('nowPoint')) {
        point.innerText = localStorage.getItem('nowPoint');
    }else {
        point.innerText = 0;
    }

    if (localStorage.getItem('nowQuizOrder') == 10) {
        finishGameBtn.style.display = 'inline';
        nextQuiz.style.display = 'none';
        
    }else if (localStorage.getItem('nowQuizOrder') >= 11) {
        window.alert('不正な操作です。回答データがリセットされます。')
        localStorage.removeItem('nowQuizOrder', quizOrder);
        localStorage.removeItem("nowPoint", nowPointCount);
        point.innerText = 0;
        location.reload();
        // if(resetOrNot) {
        //     totalPointInput.value = localStorage.getItem('nowPoint');
        //     localStorage.removeItem('nowQuizOrder', quizOrder);
        //     localStorage.removeItem("nowPoint", nowPointCount);
        //     point.innerText = 0;
        // }
    }

});

finishGameBtn.addEventListener('click', () => {
    totalPointInput.value = localStorage.getItem('nowPoint');
    localStorage.removeItem('nowQuizOrder', quizOrder);
    localStorage.removeItem("nowPoint", nowPointCount);
    point.innerText = 0;
})

newGame.addEventListener('click', () => {
    localStorage.removeItem('nowQuizOrder', quizOrder);
    localStorage.removeItem("nowPoint", nowPointCount);
    point.innerText = 0;
    location.reload();
})

resetBtn.addEventListener('click', () => {
    localStorage.removeItem('nowQuizOrder', quizOrder);
    localStorage.removeItem("nowPoint", nowPointCount);
    point.innerText = 0;
})




