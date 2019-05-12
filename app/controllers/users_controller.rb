class UsersController < ApplicationController
  def show
    @user = User.find(params[:id])x
    byebug
  end

  def new

  end
end
