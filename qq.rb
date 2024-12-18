require 'octokit'
require 'git'

# Сохранение данных в файл
def save_credentials(username, token)
  File.open("credentials.txt", "w") do |file|
    file.puts("Username: #{username}")
    file.puts("Token: #{token}")
  end
  puts "Credentials saved to credentials.txt"
end

# Подключение к GitHub с использованием токена
def connect_to_github(username, token)
  client = Octokit::Client.new(login: username, token: token)
  begin
    client.user # Пытаемся получить данные о пользователе
    puts "Connected to GitHub as #{username}"
    return client
  rescue Octokit::Unauthorized
    puts "Invalid credentials. Please try again."
    exit
  end
end

# Загрузка файла в репозиторий
def upload_to_github(client, file_path, repo_name, commit_message)
  # Путь к файлу для загрузки
  file_name = File.basename(file_path)

  # Чтение содержимого файла
  file_content = File.read(file_path)
  
  # Загружаем файл на GitHub
  begin
    client.create_contents(
      repo_name, 
      commit_message, 
      file_name, 
      file_content, 
      branch: 'main' # Используйте нужную ветку, если это не main
    )
    puts "File #{file_name} uploaded successfully to #{repo_name}!"
  rescue Octokit::UnprocessableEntity => e
    puts "Error uploading file: #{e.message}"
  end
end

# Функция для использования git
def git_push(local_repo_path)
  begin
    repo = Git.open(local_repo_path)
    repo.add(all: true)
    repo.commit('Automatic commit from Ruby script')
    repo.push
    puts "Changes pushed to GitHub repository!"
  rescue => e
    puts "Error during git push: #{e.message}"
  end
end

# Основная логика
puts "Enter your GitHub username:"
username = gets.chomp

puts "Enter your GitHub token:"
token = gets.chomp

save_credentials(username, token)  # Сохраняем учетные данные

# Подключаемся к GitHub
client = connect_to_github(username, token)

# Репозиторий, куда будем загружать файлы
repo_name = "Lapenizo/Z"  # Используем репозиторий Lapenizo/Z

# Спрашиваем у пользователя, что он хочет загрузить
puts "Enter the local file path to upload to GitHub:"
file_path = gets.chomp

puts "Enter a commit message:"
commit_message = gets.chomp

# Загружаем файл в репозиторий
upload_to_github(client, file_path, repo_name, commit_message)

# Пытаемся выполнить git push
puts "Do you want to push your changes to a local Git repository? (y/n)"
answer = gets.chomp
if answer.downcase == 'y'
  puts "Enter the path to your local Git repository:"
  local_repo_path = gets.chomp
  git_push(local_repo_path)
end