<?php

// $key= 123;
// $userid = 9876;
// https://www.goodreads.com/review/list?v=2&key=$key&id=$userid&shelf=read&per_page=200
// save that to myreviews.xml

date_default_timezone_set('UTC');
$xml = simplexml_load_file("myreviews.xml", 'SimpleXMLElement', LIBXML_NOCDATA);
$j = json_encode($xml);
$o = json_decode($j);

foreach ($o->reviews->review as $rev) {
	print book_title_slug($rev->book->title) . "\n";
	print "Read dates: " . format_date($rev->started_at) . " until " . format_date($rev->read_at) . "\n"; 

	$rating = (int) $rev->rating;
	print "$rating stars\n";

	$review = html_to_md($rev->body);
	print "$review\n";
}

function html_to_md($body) {
	if (!$body || !is_string($body)) {
		return "no review!";
	}

	$answer = $body;
	$answer = str_replace("<br />", "\n\n", $answer);
	$answer = str_replace("<i>", "_", $answer);
	$answer = str_replace("</i>", "_", $answer);
	$answer = preg_replace('~<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>~', '[\\2](\\1)', $answer);
	$answer = trim($answer);
	return $answer;
}

function format_date($datedesc) {
	if (!$datedesc) {
		return '';
	}

	$ts = strtotime($datedesc);
	return date('Y-m-d', $ts);
}

function book_title_slug($title) {
	$answer = $title;

	$answer = cut_out_parens($answer);
	$answer = cut_out_subtitle($answer);
	$answer = cut_out_nonalphanum($answer);
	$answer = strtolower(trim($answer));
	$answer = dash_for_space($answer);

	return $answer;
}

function cut_out_parens($title) {
	return preg_replace('~\(.*\)~', '', $title);
}

function cut_out_subtitle($title) {
	return preg_replace('~:.*$~', '', $title);
}

function cut_out_nonalphanum($title) {
	return preg_replace('~[^A-Za-z0-9\s]~', '', $title);
}

function dash_for_space($title) {
	return preg_replace('~\s+~', '-', $title);
}