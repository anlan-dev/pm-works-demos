$content = Get-Content "g:\POLYU\2026-2027找工作\demo\work\index.html" -Raw -Encoding UTF8

$aigcCard = '<div id="project-aigc" class="project-card-wrap scroll-margin"><a class="project-card-hit" href="#aigc-showcase"><div class="project-emoji">&#10024;</div><div class="project-title">AIGC 能力展示 <span class="project-highlight">&#22810;&#22330;&#26223; &#183; &#22810;&#24179;&#21488;</span></div><div class="project-subtitle">AI &#28789;&#24863;&#29983;&#25104; &#183; AI &#21095;&#24773;&#29983;&#25104; &#183; AI &#21019;&#24847;&#35786;&#26029; &#183; Prompt &#24211;</div><div class="project-desc">&#27178;&#36328;&#21019;&#20316;&#33329;&#12289;&#21095;&#26412;&#33329;&#12289;&#20912;&#21551;&#21160;&#12289;Prompt Library &#31561;&#22810;&#20010;&#39033;&#30446;&#65292;&#23637;&#31034; AIGC &#22312;&#20135;&#21697;&#20013;&#30340;&#35268;&#21010;&#24605;&#36335;&#19982;&#20132;&#20114;&#21407;&#22411;&#35774;&#35745;&#12290;</div><div><span class="project-tag">AIGC</span><span class="project-tag">Prompt Engineering</span><span class="project-tag">&#22810;&#24179;&#21488;&#25509;&#20837;</span><span class="project-tag">&#20132;&#20114;&#21407;&#22411;</span></div></a><div class="project-entry-row"><a class="project-entry-btn result" href="#aigc-showcase">&#20808;&#30475;&#32467;&#26524;</a></div></div>'

$searchStr = [char]0x4F53 + [char]0x9A8C + ' Demo</a></div></div><div id="deep-case-studies"'
$idx = $content.IndexOf($searchStr)
Write-Host "Full search at: $idx"

$partialStr = [char]0x4F53 + [char]0x9A8C + ' Demo</a></div></div>'
$idx2 = $content.IndexOf($partialStr)
Write-Host "Partial search at: $idx2"

if ($idx2 -gt 0) {
    $context = $content.Substring($idx2, [Math]::Min(300, $content.Length - $idx2))
    Write-Host "Context: $context"
}