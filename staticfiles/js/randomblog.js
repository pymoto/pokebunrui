const nextbtn = document.getElementById('nextbtn')

nextbtn.addEventListener('click', () => {
    location.reload();
})



const minimumDistance = 30
// スワイプ開始時の座標
let startX = 0
let startY = 0
// スワイプ終了時の座標
let endX = 0
let endY = 0

// 解説①：移動を開始した座標を取得
window.addEventListener('touchstart', (e) =>  {
  startX = e.touches[0].pageX
  startY = e.touches[0].pageY
})

// 解説②：移動した座標を取得
window.addEventListener('touchmove', (e) =>  {
  endX = e.changedTouches[0].pageX
  endY = e.changedTouches[0].pageY
})


// 解説③：移動距離から左右or上下の処理を実行
window.addEventListener('touchend', (e) =>  {
  // スワイプ終了時にx軸とy軸の移動量を取得
  // 左スワイプに対応するためMath.abs()で+に変換
  const distanceX = Math.abs(endX - startX)
  const distanceY = Math.abs(endX - startY)

  // 左右のスワイプ距離の方が上下より長い && 小さなスワイプは検知しないようにする
  if (distanceX > distanceY && distanceX > minimumDistance) {
    // スワイプ後の動作
    console.log('左右スワイプ')
    location.reload();
  }
  
  // 上下のスワイプ距離の方が左右より長い && 小さなスワイプは検知しないようにする
  if (distanceX < distanceY && distanceY > minimumDistance) {
    // スワイプ後の動作
    console.log('上下スワイプ')
  }
})