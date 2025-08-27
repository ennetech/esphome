#pragma once

#include "esphome/components/select/select.h"
#include "../dfrobot_sen0623.h"

namespace esphome {
namespace dfrobot_sen0623 {

class Sen0623ModeSelect : public select::Select, public Parented<DfrobotSen0623Component> {
 public:
  Sen0623ModeSelect() = default;

 protected:
  void control(const std::string &value) override;
};

}  // namespace dfrobot_sen0623
}  // namespace esphome
