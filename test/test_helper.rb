ENV['RAILS_ENV'] ||= 'test'
require File.expand_path('../../config/environment', __FILE__)
require 'rails/test_help'

class ActiveSupport::TestCase
  # Setup all fixtures in test/fixtures/*.yml for all tests in alphabetical order.
  fixtures :all
  include ApplicationHelper
  # テストユーザーがログイン中の場合にtrueを返す。名前はis_logged_in?
  def is_logged_in?# rubocop:disable all
    !session[:user_id].nil?
  end
end
