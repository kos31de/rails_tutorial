if Rails.env.production?
  CarrierWave.configure do |config|
    config.fog_provider = 'fog/aws'
    config.fog_credentials = {
      # Amazon S3用の設定
      :provider              => 'AWS',
      :region                => ENV['ap-northeast-1'],
      :aws_access_key_id     => ENV['AKIAQK6J3SGT54Q6V7JK'],
      :aws_secret_access_key => ENV['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']
    }
    config.fog_directory     =  ENV['S3_BUCKET']
  end
end
