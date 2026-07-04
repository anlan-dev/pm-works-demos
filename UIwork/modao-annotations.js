/* ============================================
   墨刀原型标注系统 · Mockplus Annotation System
   版本: v1.0
   用法: 在HTML中定义 window.MODAO_ANNOTATIONS 数组
   然后引入本文件即可
   ============================================ */

(function(){

  // 如果页面没有自定义标注，使用空数组
  var ANNOS = window.MODAO_ANNOTATIONS || [];

  // ---- DOM 引用 ----
  var toggleBtn, annoContainer, legendEl;

  function init(){
    toggleBtn = document.getElementById('modaoToggle');
    annoContainer = document.getElementById('modaoAnno');
    legendEl = document.getElementById('modaoLegend');

    if(!toggleBtn || !annoContainer) return;

    // 如果外部没定义标注，自动从页面 .modao-anno-item 元素读取
    if(ANNOS.length === 0){
      document.querySelectorAll('.modao-anno-item').forEach(function(el){
        ANNOS.push({
          sel: el.getAttribute('data-target'),
          text: el.getAttribute('data-text'),
          cat: el.getAttribute('data-cat') || '设计决策',
          cls: el.getAttribute('data-cls') || 'doc',
          pos: el.getAttribute('data-pos') || 'top'
        });
      });
    }

    buildAnnotations();
  }

  function buildAnnotations(){
    annoContainer.innerHTML = '';
    ANNOS.forEach(function(item, i){
      var el = document.querySelector(item.sel);
      if(!el) return;

      // 编号圆点
      var dot = document.createElement('div');
      dot.className = 'modao-anno-dot';
      dot.innerHTML = '<span class="num">' + (i+1) + '</span>';
      dot.setAttribute('data-index', i);
      dot.onclick = function(){ scrollToAnno(i); };
      annoContainer.appendChild(dot);

      // 标注卡片
      var card = document.createElement('div');
      card.className = 'modao-anno-card';
      card.innerHTML = '<div class="connector-top"></div>'
        + '<span class="cat ' + item.cls + '">' + item.cat + '</span>'
        + '<p>' + item.text + '</p>';
      card.style.display = 'none';
      card.setAttribute('data-index', i);
      card.onclick = function(){ scrollToAnno(i); };
      annoContainer.appendChild(card);
    });
    positionAnnotations();
  }

  function positionAnnotations(){
    var dots = annoContainer.querySelectorAll('.modao-anno-dot');
    var cards = annoContainer.querySelectorAll('.modao-anno-card');
    ANNOS.forEach(function(item, i){
      var el = document.querySelector(item.sel);
      if(!el) return;
      var rect = el.getBoundingClientRect();
      var dot = dots[i]; if(!dot) return;
      var card = cards[i]; if(!card) return;

      var dotSize = 40;
      dot.style.left = (rect.left + rect.width/2 - dotSize/2) + 'px';
      dot.style.top = (rect.top + rect.height/2 - dotSize/2) + 'px';

      card.style.display = 'block';
      var cardW = 220, gap = 16, cLeft, cTop;
      if(item.pos === 'bottom'){
        cLeft = rect.left + rect.width/2 - cardW/2;
        cTop = rect.bottom + gap;
      } else {
        cLeft = rect.left + rect.width/2 - cardW/2;
        cTop = rect.top - gap - 60;
      }
      if(cLeft < 10) cLeft = 10;
      if(cLeft + cardW > window.innerWidth - 10) cLeft = window.innerWidth - cardW - 10;
      if(cTop < 10) cTop = rect.bottom + gap;
      if(cTop + 60 > window.innerHeight - 10) cTop = rect.top - gap - 60;
      card.style.left = cLeft + 'px';
      card.style.top = cTop + 'px';
    });
  }

  function scrollToAnno(index){
    var item = ANNOS[index];
    if(!item) return;
    var el = document.querySelector(item.sel);
    if(el) el.scrollIntoView({behavior:'smooth',block:'center'});
  }

  window.toggleModao = function(){
    var active = toggleBtn.classList.toggle('active');
    if(active){
      toggleBtn.innerHTML = '<span class="dot"></span> 关闭标注';
      document.body.classList.add('modao-mode');
      setTimeout(function(){ legendEl && legendEl.classList.add('show'); }, 300);
      positionAnnotations();
    } else {
      toggleBtn.innerHTML = '<span class="dot"></span> 墨刀原型标注';
      document.body.classList.remove('modao-mode');
      legendEl && legendEl.classList.remove('show');
    }
  };

  window.addEventListener('resize', function(){
    if(toggleBtn.classList.contains('active')) positionAnnotations();
  });

  // DOM ready 后初始化
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
