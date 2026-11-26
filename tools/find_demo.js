// Open a Slotslaunch game page, press its free-play button and print the game frame's address chain.
const { chromium } = require('playwright');
(async () => {
  const url = process.argv[2];
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1280, height: 800 }, userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36' });
  const p = await ctx.newPage();
  const hosts = {};
  p.on('request', r => { try { const h = new URL(r.url()).host; hosts[h] = (hosts[h]||0)+1; } catch {} });
  const resp = await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  console.log('status', resp.status());
  await p.waitForTimeout(3000);
  const btns = await p.$$eval('button, a', els => els.map(e => (e.innerText||'').trim()).filter(t => /play|demo|free/i.test(t)).slice(0, 12));
  console.log('buttons', JSON.stringify(btns));
  for (const sel of ['button.js-free-play', 'text=/play (for )?free/i', 'text=/free play/i', 'text=/play demo/i', '.play-button', '#play-button', 'button:has-text("Play")']) {
    const el = await p.$(sel);
    if (el) { try { await el.click({ timeout: 4000 }); console.log('clicked', sel); break; } catch (e) { console.log('click failed', sel); } }
  }
  await p.waitForTimeout(Number(process.argv[3] || 20000));
  for (const f of p.frames()) console.log('frame', f.url().replace(/([?&](?:mgckey|token|session|sessionid|sid|key|auth|jwt)=)[^&#]*/gi, '$1…').slice(0, 400));
  console.log('hosts', JSON.stringify(Object.entries(hosts).sort((a,b)=>b[1]-a[1]).slice(0,15)));
  await p.screenshot({ path: process.argv[4] || '/dev/null' }).catch(()=>{});
  await b.close();
})();
