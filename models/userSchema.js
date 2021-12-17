import mongoose from "mongoose";

const userSchema = mongoose.Schema(
  {
    username: {
      type: String,
    },
    email: {
      type: String,
    },
    password: {
      type: String,
    },
    userpfp: {
      type: String,
    },
    followers: {
      type: Array,
      default: [],
    },
    following: {
      type: Array,
      default: [],
    },
    pastes: {
      type: Array,
      default: [],
    },
  },
  { timestamps: true }
);

const User = mongoose.model("user", userSchema);

export default User;
