const out=document.querySelector("#output");const statusEl=document.querySelector("#status");
async function health(){try{const r=await fetch("/api/health");const j=await r.json();statusEl.textContent=j.ok?"接続中":"エラー"}catch{statusEl.textContent="未接続"}}
async function run(name){out.textContent="実行中…";try{const r=await fetch("/api/run/"+encodeURIComponent(name));const j=await r.json();out.textContent=j.output||j.error||JSON.stringify(j,null,2)}catch(e){out.textContent="通信エラー: "+e}}
document.querySelectorAll("[data-run]").forEach(b=>b.addEventListener("click",()=>run(b.dataset.run)));
document.querySelector("#clear").addEventListener("click",()=>out.textContent="");
health();
