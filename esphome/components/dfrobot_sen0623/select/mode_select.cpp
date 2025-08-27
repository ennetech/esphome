#include "mode_select.h"

namespace esphome {
namespace dfrobot_sen0623 {

void Sen0623ModeSelect::control(const std::string &value) {
  this->publish_state(value);
  if (value == "fall") {
    this->parent_->set_mode(SEN0623_MODE_FALL);
  } else if (value == "sleep") {
    this->parent_->set_mode(SEN0623_MODE_SLEEP);
  }
}

}  // namespace dfrobot_sen0623
}  // namespace esphome
