<?php

	# Content-type を出力
	// header("Content-type:text/plain");
	header("Content-type:text/plain;charset=utf-8");

	# 名前を指定してファイル情報を取得する
	$input_file = $_FILES["input_file"];//コントロール名を取得する
  // echo "name:" . $input_file["name"] . "\n";
  // echo "type:" . $input_file["type"] . "\n";
  // echo "size:" . $input_file["size"] . "\n";
  // echo "tmp_name:" . $input_file["tmp_name"] . "\n";
  // echo "error:" . $input_file["error"] . "\n";

	# 拡張子を取得する
	$file_ext = pathinfo($input_file["name"], PATHINFO_EXTENSION);


	# アップロード可能な拡張子であるか調べる
	if(FileExtensionGetAllowUpload($file_ext)){
    // exho "save input file \n"
		# 現在の時間を取得する
		$time_now = time();

		# 保存先のファイルパスを生成する（実戦運用する場合、排他処理を考慮して保存先のファイル名を生成する必要があります）
		// $file_name_new = "./../python/" . $time_now . "." . $file_ext;
		$file_name_new = "./../python/receive_file." . $file_ext;

		# ファイルの移動を行う
		move_uploaded_file ($input_file["tmp_name"], $file_name_new);
    // $user_name = "atsushikawakubo@outlook.jp";
    // chown($path, $user_name);
    // $user_name = "root";
		$file_name_copy = "./../python/". $time_now . "." . $file_ext;
		$flg = copy($file_name_new, $file_name_copy);
    chmod($file_name_copy, 0777);
	}


	#// -----------------------------------------------------
	#// 拡張子からアップロードを許すか調べる
	#// -----------------------------------------------------
	function FileExtensionGetAllowUpload($ext){

		# アップロードを許可したい拡張子があればここに追加
		$allow_ext = array("py","txt");

		foreach($allow_ext as $v){
			if ($v === $ext){
				return 1;
			}
		}

		return 0;
	}

?>
