# MCE 503 — Digital Signals and Modelling

*3 Units · 500 Level, Harmattan · BMAS: MCT 503 · FUTO Mechatronics*

## Overview

This course turns a continuous sensor signal into numbers a processor can use, and gives you the mathematics to prove the result still means what went in. The chain: sample → quantise → model as a discrete system → analyse in frequency → filter → implement. Every exam question sits on that chain.

Paper: 2½–3 hours, **answer 5 of 6, at least two from each of two sections**, 20 marks each. Parts are 2–10 marks (define, sketch, derive, compute).

## Synopsis (BMAS, verbatim)

> "The concepts of sampling, quantization and aliasing. Discrete time signals and systems, discrete convolution, Z transforms, Z plane poles and zeros. Discrete Fourier transforms. Fast Fourier Transform. Concept of digital filtering, types of digital filters and properties. Digital transfer functions. One dimensional recursive and non recursive filters. Spectral transforms and their application in synthesis of high-pass and band-pass filters. Computer techniques in filter synthesis. Realization of filters in hardware and software. Basic image processing concepts."

## Sources

- **Li Tan & Jiang, _Digital Signal Processing_ (Drive folder PDF)** — the taught text, and it uses the one-sided z-transform the papers use. Ch. 2 sampling (pp. 15–56); Ch. 3 signals and systems (pp. 57–86); Ch. 4 DFT/FFT (pp. 87–136); Ch. 5 z-transform (pp. 137–160); Ch. 6 filtering and realisation (pp. 161–216); Ch. 7 FIR design (pp. 217–300); Ch. 8 IIR design (pp. 301–404); Ch. 9 hardware (pp. 405–452); Ch. 14 image basics (p. 683 ff.).
- **Proakis & Manolakis, _DSP_ (Drive folder PDF, 3rd ed.)** — extra rigour and worked examples: Ch. 1 §1.4 sampling and quantisation; Ch. 2 discrete-time signals and systems; Ch. 3 the z-transform; Ch. 4–5 frequency analysis and the DFT; Ch. 7 realisation structures; Ch. 8 filter design.
- **Heckbert, _Fourier Transforms and the FFT_** (taught handout) — CTFT → DFT → FFT → 2-D DFT; the only notes that match the FFT/butterfly question.
- **`ZTransformPractice.pdf`** (Drive folder) — drill set for inverse z and pole-zero plots.
- **Past papers:** 2019/2020, 2020/2021, 2021/2022. The 2021/22 paper is split into Section A and Section B.
- **Online:** [MIT 6.003](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) — Lecture 5 (z-transform), Lectures 17–19 (DT Fourier and DFT), Lectures 21–22 (sampling and quantisation); [The Scientist and Engineer's Guide to DSP](https://www.dspguide.com/) — Ch. 3 (ADC/DAC), Ch. 10–12 (Fourier/FFT), Ch. 14–16 (filters).
- **Gap:** image processing has no taught material; low priority.
- **Not included:** textbooks and lecturer notes are not redistributed here; see [`docs/sources.md`](../docs/sources.md).

## Course Content Summary

| Concept | Importance | Exam likelihood |
|---|---|---|
| Sampling & aliasing | Essential | **Very high** (3/3) |
| Quantisation & PCM | Essential | Medium (2/3) |
| Signals & sequences | Essential | High (2/3) |
| LTI systems, convolution, difference equations | Essential | High (2/3) |
| z-transform, ROC, properties, inverse z | Essential | **Very high** (2/3) |
| Poles, zeros, stability, eigenfunctions | Essential | **Very high** (3/3) |
| DTFT / DFT / FFT | Important | Medium (1/3) |
| Filter types & specification | Important | Medium (1/3) |
| IIR/FIR design, spectral transforms | Important | Low (0/3), BMAS-mandated |
| Realisation & word length | Supporting | Low (2/3 diagrams) |
| Image processing basics | Important | Unknown (0/3) |

## Course Content Details

### 1. Signals, sequences and discrete systems

Discrete signals exist only at integer instants: sinusoids are periodic only when $\omega_0/2\pi$ is rational, and high frequencies can masquerade as low ones. A system is fully characterised by its impulse response.

**Study:** Li Tan Ch. 3 §3.1–3.5 (pp. 57–79); Proakis Ch. 2 §2.1–2.3 (pp. 43–78); [MIT 6.003 Lectures 1–2 and 8](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) (DT signals, convolution).
**Exam:** 2021/22 Sec B Q1(a)–(b), Q3(a)–(d); 2020/21 Q1(b), Q3(a).

- [ ] **Signal classes** — continuous $x(t)$ vs discrete $x[n]$ vs digital (time, amplitude, value set); two examples each.
- [ ] **Elementary sequences** — $\delta[n]$, $u[n]$, ramp, $a^n u[n]$ (all ranges of $a$), complex exponential, sinusoid: definition and sketch.
- [ ] **Properties** — periodicity $x[n+N]=x[n]$ with $N=2\pi/\omega_0$; even/odd decomposition; energy and power; absolute summability.
- [ ] **Operations** — shift, fold, scale, decimate by $M$, interpolate by $L$; fold-then-shift vs shift-then-fold.
- [ ] **LTI tests** — superposition and time-invariance, with counter-examples $x^2[n]$, $n\,x[n]$, $x[n]+x[n-1]$.
- [ ] **Convolution** — graphical method and the sum
  $$y[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k]$$
  Output length $L_1+L_2-1$; circular convolution and the zero-padding remedy.

### 2. Sampling, aliasing and quantisation

The highest-yield block. Sampling replicates the spectrum every $F_s$; if replicas overlap, information is destroyed and no filter recovers it.

**Study:** Li Tan Ch. 2 §2.1–2.3 (pp. 15–46); Proakis Ch. 1 §1.4 (pp. 21–39); [MIT 6.003 Lectures 21–22](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/); dspguide Ch. 3.
**Exam:** 2020/21 Sec B Q1(b), Q2(a)–(b); 2021/22 Sec A Q1(a)–(b), Q2(b)–(c); 2019/20 Q2 (aliasing of a sinusoid).

- [ ] **Ideal sampling** — impulse-train model; the spectrum replicates every $\Omega_s$:
  $$X_p(j\Omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X\!\left(j(\Omega-k\Omega_s)\right),\qquad \Omega_s=\frac{2\pi}{T}$$
  Sketch the three cases $F_s>2F_{\max}$, $F_s=2F_{\max}$, $F_s<2F_{\max}$.
- [ ] **Theorem** — Nyquist rate $2F_{\max}$, folding frequency $F_s/2$, strict inequality, band-limited premise.
- [ ] **Aliasing** — a component above Nyquist folds to
  $$f_{\text{alias}}=\left|f-kF_s\right|$$
  Tabulate the replicas and explain why the fold is irreversible.
- [ ] **Reconstruction** — sinc interpolation, zero-order-hold droop, anti-image filter, anti-alias filter before the sampler.
- [ ] **Quantisation** — step size, error power and SNR for a $b$-bit converter:
  $$\Delta=\frac{R}{2^b},\qquad \sigma_e^2=\frac{\Delta^2}{12},\qquad \mathrm{SNR}\approx 6.02b+1.76\ \text{dB}$$
  Cover overload and companding ($\mu$-law and A-law).
- [ ] **PCM/A-D chain** — sample → quantise → encode; block diagram with each block's function.

### 3. LTI systems in the z-domain

The z-transform turns convolution into multiplication and difference equations into algebra. The ROC, not the formula, decides stability.

**Study:** Li Tan Ch. 5 §5.1–5.4 (pp. 137–156); Proakis Ch. 3; [MIT 6.003 Lecture 5](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) (z-transform) and Lecture 3 (poles and modes).
**Exam:** 2020/21 Q1(a), Q1(c), Q2(c); 2021/22 Sec B Q2(a)–(d), Q4(a)–(c).

- [ ] **Definition and ROC** — two-sided vs one-sided, four ROC shapes, no poles in the ROC, ROC must be connected.
- [ ] **Standard pairs** — derive each from the geometric series:
  $$\delta[n]\leftrightarrow 1,\qquad u[n]\leftrightarrow\frac{1}{1-z^{-1}},\qquad a^n u[n]\leftrightarrow\frac{1}{1-az^{-1}}$$
  $$-a^n u[-n-1]\leftrightarrow\frac{1}{1-az^{-1}},\qquad n\,u[n]\leftrightarrow\frac{z^{-1}}{(1-z^{-1})^2}$$
  Also $n^2u[n]$ and $\cos(\omega_0 n)u[n]$, with their ROCs.
- [ ] **Properties** — linearity, two-sided and one-sided shift (prove $n-2$), scaling, differentiation, convolution, initial/final value, with ROC caveats.
- [ ] **Inverse z** — long division, partial fractions (distinct, repeated, complex poles), tables; divide by $z$ before expanding.
- [ ] **System function** — from a difference equation and back:
  $$H(z)=\frac{B(z)}{A(z)}=\frac{\sum_{k=0}^{M}b_k z^{-k}}{1+\sum_{k=1}^{N}a_k z^{-k}}$$
  State the order and draw the direct-form diagram.
- [ ] **Poles and zeros** — plot with the unit circle, note multiplicity, and read the magnitude as a distance ratio:
  $$\left|H(e^{j\omega})\right|=\frac{\prod_{k}\left|e^{j\omega}-z_k\right|}{\prod_{k}\left|e^{j\omega}-p_k\right|}$$
  A zero at $z=1$ kills DC; a zero at $z=-1$ kills Nyquist.

### 4. Stability and the eigenfunction method

The most repeated idea: from a difference equation produce $H(z)$, the pole-zero plot, a stability verdict, and the output for input $z_0^n$.

**Study:** Li Tan Ch. 6 §6.2–6.4 (pp. 166–185); Proakis Ch. 3; `ZTransformPractice.pdf`; [MIT 6.003 Lecture 3](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).
**Exam:** 2020/21 Q1(c), Sec B Q3(a)–(b); 2021/22 Sec A Q3(a)–(b); 2019/20 Q3–Q4.

- [ ] **Stability criterion** — causal ⇒ all poles strictly inside the unit circle; on the circle marginal, outside unstable; ROC contains the unit circle.
- [ ] **Eigenfunction property** — for $z_0$ inside the ROC:
  $$x[n]=z_0^n\ \Longrightarrow\ y[n]=H(z_0)\,z_0^n$$
  Superpose for sums of exponentials.
- [ ] **Pole-zero sketching** — poles ×, zeros ○, labelled unit circle, shaded ROC, stability stated in words.
- [ ] **Benchmark** — analyse
  $$y[n]=x[n]-x[n-1]-1.1y[n-1]-0.28y[n-2]$$
  Find $H(z)$, $A(z)$, $B(z)$, the poles ($-0.4$, $-0.7$), the zeros ($0$, $1$), stability, and the first five terms of $h[n]$.
- [ ] **Benchmark** — for
  $$H(z)=\frac{z}{z-\tfrac12},\qquad x[n]=\left(\tfrac13\right)^n+3(2)^n$$
  the eigenfunction method gives $y[n]=-2\left(\tfrac13\right)^n+4(2)^n$.

### 5. Frequency-domain analysis: DTFT, DFT, FFT

The DTFT is theory, the DFT is what a computer does, the FFT is why it is affordable. The DFT is the z-transform on the unit circle.

**Study:** Heckbert handout (the whole document — the DFT→FFT derivation and the 2-D DFT are the parts that matter); Li Tan Ch. 4 §4.1–4.5 (pp. 87–131); Proakis Ch. 4–5; [MIT 6.003 Lectures 17–19](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).
**Exam:** 2020/21 Q3(b) (4-point butterfly); 2019/20 Q1(a)–(b) (impulse-train spectrum).

- [ ] **DTFT** — definition and inverse:
  $$X(e^{j\omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\omega n},\qquad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\omega})e^{j\omega n}\,d\omega$$
  Note the $2\pi$-periodicity, existence by absolute summability, and symmetry for real signals.
- [ ] **DFT** — with $W_N=e^{-j2\pi/N}$:
  $$X[k]=\sum_{n=0}^{N-1}x[n]W_N^{kn},\qquad x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]W_N^{-kn}$$
  $X[k]=X(e^{j2\pi k/N})$; resolution $\Delta f=F_s/N$.
- [ ] **Three routes** — direct sum, matrix form and radix-2 butterfly:
  $$\mathbf{X}=\mathbf{W}\mathbf{x}$$
  All three must give the same answer for $N=4$.
- [ ] **FFT** — decimation-in-time butterfly and cost:
  $$p'=p+W_N^r q,\qquad q'=p-W_N^r q$$
  $\log_2 N$ stages, bit-reversed input; $N^2$ vs $\frac{N}{2}\log_2 N$ operations (about $205\times$ fewer at $N=1024$).
- [ ] **Leakage** — rectangular vs Hann/Hamming/Blackman, main vs side lobe, why you window before an FFT.

### 6. Digital filters: types and specification

A filter is a frequency-selective gain. Ideal responses are unrealisable (infinite, non-causal sincs), so every design trades transition width against order.

**Study:** Li Tan Ch. 6 §6.1–6.5 (pp. 161–191); Proakis Ch. 8 §8.1; dspguide Ch. 14–16 (filter types, moving average, windowed-sinc).
**Exam:** 2020/21 Q2(a)–(b).

- [ ] **Ideal responses** — sketch LP, HP, BP, BS with arbitrary cutoff; ideal sinc $h[n]$; explain unrealisability.
- [ ] **Specification** — passband/stopband edges, ripple $\delta_p$ ($A_p$ dB), attenuation $\delta_s$ ($A_s$ dB), transition width.
- [ ] **Prototypes** — Butterworth (maximally flat), Chebyshev I/II, elliptic; compare order for the same spec.
- [ ] **IIR design** — bilinear transform and frequency warping:
  $$s=\frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}},\qquad \Omega=\frac{2}{T}\tan\frac{\omega}{2}$$
  Pre-warp the critical frequency; know why impulse invariance fails for high-pass designs.
- [ ] **FIR design** — sinc × window, window from attenuation, $N$ from transition width, Gibbs, frequency sampling.
- [ ] **Linear phase** — symmetry ⇒ exact linear phase, delay $(N-1)/2$, four types, which cannot do high-pass.

### 7. Spectral transformation and filter synthesis

BMAS is unusually specific here, which usually means it was taught. Expect a prototype-transformation question even though no paper has asked one.

**Study:** Li Tan Ch. 7 (FIR, pp. 217–300) and Ch. 8 (IIR, pp. 301–404) — the design recipes only; Proakis Ch. 8.
**Exam:** No direct question; needed if Q2(b) asks for a filter sketch or design.

- [ ] **LP → HP** — replace $s$ and move the cutoff:
  $$s\;\longrightarrow\;\frac{\Omega_c^2}{s}$$
  Check the new cutoff and the stopband.
- [ ] **LP → BP** — the band-pass transformation:
  $$s\;\longrightarrow\;\frac{s^2+\Omega_0^2}{Bs}$$
  Band edges, centre frequency, bandwidth.
- [ ] **LP → BS** — reciprocal transformation; notch edges.
- [ ] **Computer techniques** — MATLAB `butter`/`cheby1`/`ellip`/`bilinear`/`fir1`/`freqz`; design flow as an exam paragraph.
- [ ] **Verification** — order, pole positions, $|H|$ at DC and Nyquist, stopband attenuation against spec.

### 8. Realisation: hardware, software, word length

A transfer function is mathematics; realisation is where it meets fixed-point arithmetic — and where a stable design can become unstable.

**Study:** Li Tan Ch. 6 §6.6 (pp. 192–199) and Ch. 9 (pp. 405–452); Proakis Ch. 7 (realisation structures).
**Exam:** 2020/21 Q1(d); 2021/22 Sec B Q1(a).

- [ ] **Direct forms** — draw I and II from $H(z)$; delays $N+M$ vs $\max(N,M)$; diagram ↔ equation.
- [ ] **Cascade and parallel** — biquads, partial fractions, why cascade at high order.
- [ ] **Hardware vs software** — DSP chip (Harvard, MAC), FPGA (parallel MAC), CPU loop; MACs per sample.
- [ ] **Real-time constraint** — multiply-accumulate budget vs $F_s$; circular buffers.
- [ ] **Word length** — coefficient quantisation moves poles, round-off noise, overflow/saturation, limit cycles.

### 9. Basic image processing

An image is a 2-D sampled, quantised array: every idea returns with two indices — sampling = pixel pitch, filtering = mask convolution, frequency = 2-D DFT/DCT.

**Study:** Li Tan Ch. 14 (p. 683 ff., §14.1–14.3 only); Heckbert's 2-D DFT section.
**Exam:** No question in the three papers — study last.

- [ ] **Image formation** — sampling (resolution) vs quantisation (bit depth), grayscale/RGB, storage calculation, moiré.
- [ ] **Histograms** — equalisation through the CDF:
  $$s=T(r),\qquad s_k=(L-1)\sum_{j=0}^{k}\frac{n_j}{N}$$
  Also contrast stretching and point operations.
- [ ] **Spatial filtering** — averaging/Gaussian, Laplacian/unsharp, median for salt-and-pepper.
- [ ] **Edges** — Sobel/Prewitt masks, Laplacian, gradient magnitude and direction, thresholding.
- [ ] **Compression** — $8\times8$ DCT, quantisation, zig-zag, entropy coding; why DCT not DFT.

## How to use this

Each topic has a **Study** line, an **Exam** line and a checklist. Read only the cited pages, work the examples in the text, then attempt the named questions with the book closed. Tick a box only when you can reproduce the method without notes.

**Refresh before starting (no new textbook):** complex numbers — magnitude, phase, Euler form, conjugates; partial fractions — distinct, repeated and complex poles; geometric series; matrix multiplication (for the DFT matrix).

**Priority:** sampling and aliasing, z-transform and inverse z, pole-zero plots, and difference equation → transfer function appear in every paper. FFT butterflies appear once but are easy marks. Filter design and image processing are lower yield.
