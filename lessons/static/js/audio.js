/**
 * Audio Pronunciation System
 * Hệ thống phát âm cho tiếng Việt
 */

class PronunciationSystem {
  constructor() {
    this.isPlaying = false;
    this.synth = window.speechSynthesis;
    this.voiceIndex = 0;
    this.initVoices();
  }

  initVoices() {
    // Lấy danh sách giọng nói
    const voices = this.synth.getVoices();
    console.log("Available voices:", voices);

    // Ưu tiên giọng tiếng Việt nếu có
    const vietnameseVoice = voices.find((v) => v.lang.includes("vi-"));
    const femaleVoice = voices.find((v) =>
      v.name.toLowerCase().includes("female")
    );
    this.preferredVoice = vietnameseVoice || femaleVoice || voices[0];
  }

  /**
   * Phát âm một chữ/từ
   * @param {string} text - Chữ/từ cần phát âm
   * @param {number} rate - Tốc độ phát (0.5-2)
   */
  speak(text, rate = 1) {
    if (!text) return;

    // Dừng nếu đang phát
    this.synth.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.language = "vi-VN";
    utterance.rate = rate;
    utterance.pitch = 1;
    utterance.volume = 1;

    // Set voice nếu có
    if (this.preferredVoice) {
      utterance.voice = this.preferredVoice;
    }

    // Callback khi phát xong
    utterance.onstart = () => {
      this.isPlaying = true;
      this.updateButtonState(true);
    };

    utterance.onend = () => {
      this.isPlaying = false;
      this.updateButtonState(false);
    };

    utterance.onerror = (event) => {
      console.error("Speech error:", event.error);
      this.isPlaying = false;
      this.updateButtonState(false);
    };

    // Phát âm
    this.synth.speak(utterance);
  }

  /**
   * Dừng phát âm
   */
  stop() {
    this.synth.cancel();
    this.isPlaying = false;
    this.updateButtonState(false);
  }

  /**
   * Cập nhật trạng thái nút
   */
  updateButtonState(isPlaying) {
    const buttons = document.querySelectorAll("[data-audio-btn]");
    buttons.forEach((btn) => {
      if (isPlaying && btn.classList.contains("playing")) {
        btn.innerHTML = "🔊 Đang phát...";
        btn.style.opacity = "0.7";
      } else {
        btn.innerHTML = "🔊 Phát âm";
        btn.style.opacity = "1";
      }
    });
  }

  /**
   * Phát âm chữ cái từ phần tử
   */
  playFromElement(element) {
    const text = element.getAttribute("data-audio-text") || element.textContent;
    element.classList.add("playing");

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.language = "vi-VN";
    utterance.rate = 0.8;

    if (this.preferredVoice) {
      utterance.voice = this.preferredVoice;
    }

    utterance.onend = () => {
      element.classList.remove("playing");
    };

    this.synth.speak(utterance);
  }
}

// Khởi tạo hệ thống
let audioSystem = null;

document.addEventListener("DOMContentLoaded", () => {
  audioSystem = new PronunciationSystem();

  // Xử lý tất cả nút phát âm
  document.querySelectorAll("[data-audio-btn]").forEach((btn) => {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      const text = this.getAttribute("data-audio-text");
      audioSystem.speak(text);
    });
  });

  // Xử lý các phần tử có data-pronounce
  document.querySelectorAll("[data-pronounce]").forEach((el) => {
    el.style.cursor = "pointer";
    el.title = "Nhấp để phát âm";

    el.addEventListener("click", function (e) {
      e.preventDefault();
      audioSystem.playFromElement(this);
    });
  });

  // Reload voices khi chúng thay đổi
  audioSystem.synth.onvoiceschanged = () => {
    audioSystem.initVoices();
  };
});

/**
 * Hàm tiện lợi: Phát âm text
 */
function speak(text, rate = 1) {
  if (audioSystem) {
    audioSystem.speak(text, rate);
  }
}

/**
 * Hàm tiện lợi: Dừng phát âm
 */
function stopSpeech() {
  if (audioSystem) {
    audioSystem.stop();
  }
}
